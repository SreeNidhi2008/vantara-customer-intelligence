import pandas as pd
import os

print("Creating behavioral customer features...")

df = pd.read_csv("data/processed/cleaned_retail_data.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Calculate invoice-level information
invoices = (
    df.groupby(["Customer ID", "Invoice"])
    .agg(
        Order_Value=("Revenue", "sum"),
        Basket_Size=("Quantity", "sum"),
        Invoice_Date=("InvoiceDate", "min")
    )
    .reset_index()
)

# Calculate customer-level features
behavior = invoices.groupby("Customer ID").agg(
    Average_Order_Value=("Order_Value", "mean"),
    Average_Basket_Size=("Basket_Size", "mean"),
    First_Purchase=("Invoice_Date", "min"),
    Last_Purchase=("Invoice_Date", "max"),
    Total_Orders=("Invoice", "nunique")
).reset_index()

behavior["Customer_Lifetime_Days"] = (
    behavior["Last_Purchase"] - behavior["First_Purchase"]
).dt.days

# Calculate average days between purchases
intervals = (
    invoices.sort_values("Invoice_Date")
    .groupby("Customer ID")["Invoice_Date"]
    .apply(lambda dates: dates.diff().dt.days.mean())
    .reset_index(name="Average_Purchase_Interval")
)

behavior = behavior.merge(intervals, on="Customer ID", how="left")

# Save the features
os.makedirs("data/processed", exist_ok=True)

behavior.to_csv(
    "data/processed/behavioral_features.csv",
    index=False
)

print("\nBehavioral feature summary:")
print(behavior.describe().round(2))

print("\nTotal customers:", len(behavior))
print("Saved: data/processed/behavioral_features.csv")
print("Behavioral feature creation completed!")
