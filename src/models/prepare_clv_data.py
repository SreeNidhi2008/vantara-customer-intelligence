import pandas as pd
import os

print("Preparing CLV prediction dataset...")

df = pd.read_csv("data/processed/cleaned_retail_data.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Define historical and future periods
observation_end = df["InvoiceDate"].max()
cutoff = observation_end - pd.Timedelta(days=90)

historical = df[df["InvoiceDate"] <= cutoff].copy()
future = df[df["InvoiceDate"] > cutoff].copy()

# Build customer features using historical transactions only
features = historical.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (cutoff - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Revenue", "sum"),
    First_Purchase=("InvoiceDate", "min"),
    Last_Purchase=("InvoiceDate", "max"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

features["Average_Order_Value"] = (
    features["Monetary"] / features["Frequency"]
)

features["Average_Basket_Size"] = (
    features["Total_Quantity"] / features["Frequency"]
)

features["Customer_Lifetime_Days"] = (
    features["Last_Purchase"] - features["First_Purchase"]
).dt.days

features = features.drop(
    columns=["First_Purchase", "Last_Purchase", "Total_Quantity"]
)

# Calculate actual revenue during the future 90-day period
future_revenue = future.groupby("Customer ID")["Revenue"].sum()

features["Future_90_Day_Revenue"] = (
    features["Customer ID"].map(future_revenue).fillna(0)
)

# Save dataset
os.makedirs("data/processed", exist_ok=True)

features.to_csv(
    "data/processed/clv_dataset.csv",
    index=False
)

print("\nDataset shape:", features.shape)
print("\nFuture revenue summary:")
print(features["Future_90_Day_Revenue"].describe().round(2))

print("\nCustomers with future revenue:",
      (features["Future_90_Day_Revenue"] > 0).sum())

print("\nSaved: data/processed/clv_dataset.csv")
print("CLV dataset preparation completed!")
