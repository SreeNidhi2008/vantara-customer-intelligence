import pandas as pd
import os

print("Combining customer features...")

rfm = pd.read_csv("data/processed/rfm_features.csv")
behavior = pd.read_csv("data/processed/behavioral_features.csv")
segments = pd.read_csv("data/processed/customer_segments.csv")

segments = segments[["Customer ID", "Customer_Segment"]]

for data in [rfm, behavior, segments]:
    data["Customer ID"] = data["Customer ID"].astype(int)

customer_features = rfm.merge(
    behavior,
    on="Customer ID",
    how="inner"
)

customer_features = customer_features.merge(
    segments,
    on="Customer ID",
    how="left"
)

os.makedirs("data/processed", exist_ok=True)

customer_features.to_csv(
    "data/processed/customer_features.csv",
    index=False
)

print("\nDataset shape:", customer_features.shape)
print("\nDataset columns:")
print(customer_features.columns.tolist())

print("\nMissing values:")
print(customer_features.isnull().sum())

print("\nSaved: data/processed/customer_features.csv")
print("Feature combination completed!")
