
import pandas as pd
import os

print("Starting RFM analysis...")

# 1. Load cleaned dataset
df = pd.read_csv(
    "data/processed/cleaned_retail_data.csv",
    parse_dates=["InvoiceDate"]
)

print("Dataset loaded:", df.shape)

# 2. Set analysis date
analysis_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# 3. Calculate RFM metrics
rfm = df.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (analysis_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

# 4. Calculate RFM scores
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5, labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

# 5. Combined RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# 6. Save results
os.makedirs("data/processed", exist_ok=True)

rfm.to_csv(
    "data/processed/rfm_features.csv",
    index=False
)

# 7. Display results
print("\n========== RFM RESULTS ==========")

print("\nFirst 10 customers:")
print(rfm.head(10))

print("\nRFM statistics:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

print("\nTotal customers:", len(rfm))
print("\nRFM analysis completed successfully!")
print("Saved: data/processed/rfm_features.csv")
