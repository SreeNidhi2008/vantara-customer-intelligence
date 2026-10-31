import pandas as pd
import os

print("Preparing churn prediction dataset...")

# Load cleaned transaction data
df = pd.read_csv("data/processed/cleaned_retail_data.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Define observation and prediction periods
observation_end = df["InvoiceDate"].max()
feature_cutoff = observation_end - pd.Timedelta(days=90)

print("Observation end:", observation_end)
print("Feature cutoff:", feature_cutoff)

# Use only transactions before the feature cutoff
historical = df[df["InvoiceDate"] <= feature_cutoff].copy()

# Calculate features using historical transactions only
customer_data = historical.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (feature_cutoff - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Revenue", "sum"),
    First_Purchase=("InvoiceDate", "min"),
    Last_Purchase=("InvoiceDate", "max")
).reset_index()

# Calculate churn using purchases in the final 90-day period
recent = df[df["InvoiceDate"] > feature_cutoff]

recent_customers = set(recent["Customer ID"].unique())

customer_data["Churn"] = (
    ~customer_data["Customer ID"].isin(recent_customers)
).astype(int)

# Add average order value
customer_data["Average_Order_Value"] = (
    customer_data["Monetary"] / customer_data["Frequency"]
)

customer_data["Customer_Lifetime_Days"] = (
    customer_data["Last_Purchase"] - customer_data["First_Purchase"]
).dt.days

# Remove date columns before modeling
customer_data = customer_data.drop(
    columns=["First_Purchase", "Last_Purchase"]
)

# Save dataset
os.makedirs("data/processed", exist_ok=True)

customer_data.to_csv(
    "data/processed/churn_dataset.csv",
    index=False
)

print("\nChurn distribution:")
print(customer_data["Churn"].value_counts())

print("\nChurn percentages:")
print(
    (customer_data["Churn"].value_counts(normalize=True) * 100).round(2)
)

print("\nDataset shape:", customer_data.shape)
print("\nMissing values:")
print(customer_data.isnull().sum())

print("\nSaved: data/processed/churn_dataset.csv")
print("Churn dataset preparation completed!")
