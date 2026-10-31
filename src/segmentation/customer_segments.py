import pandas as pd
import os

print("Starting customer segmentation...")

rfm = pd.read_csv("data/processed/rfm_features.csv")

def segment_customer(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Champions"
    elif row["R_Score"] >= 3 and row["F_Score"] >= 4:
        return "Loyal Customers"
    elif row["R_Score"] >= 4 and row["F_Score"] <= 2:
        return "Potential Loyalists"
    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"
    elif row["R_Score"] <= 2 and row["F_Score"] <= 2:
        return "Lost Customers"
    else:
        return "Customers Needing Attention"

rfm["Customer_Segment"] = rfm.apply(segment_customer, axis=1)

print("\nCustomer segment counts:")
print(rfm["Customer_Segment"].value_counts())

print("\nRevenue by customer segment:")
print(
    rfm.groupby("Customer_Segment")["Monetary"]
    .agg(["count", "sum", "mean"])
    .round(2)
)

os.makedirs("data/processed", exist_ok=True)
rfm.to_csv("data/processed/customer_segments.csv", index=False)

print("\nCustomer segmentation completed!")
print("Saved: data/processed/customer_segments.csv")
