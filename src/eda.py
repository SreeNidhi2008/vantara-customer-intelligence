
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

file_path = "data/processed/cleaned_retail_data.csv"

print("Loading cleaned dataset...")

df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])

print("Dataset loaded!")
print("Shape:", df.shape)

# ==========================================
# 2. CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("reports/figures", exist_ok=True)

# ==========================================
# 3. MONTHLY REVENUE TREND
# ==========================================

df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = df.groupby("YearMonth")["Revenue"].sum()

plt.figure(figsize=(12, 6))
monthly_revenue.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/monthly_revenue.png")
plt.show()

# ==========================================
# 4. TOP 10 PRODUCTS
# ==========================================

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.tight_layout()
plt.savefig("reports/figures/top_products.png")
plt.show()

# ==========================================
# 5. TOP 10 COUNTRIES BY REVENUE
# ==========================================

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_countries.sort_values().plot(kind="barh")
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("reports/figures/top_countries.png")
plt.show()

# ==========================================
# 6. TOP 10 CUSTOMERS BY REVENUE
# ==========================================

top_customers = (
    df.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 customers by revenue:")
print(top_customers)

# ==========================================
# 7. SUMMARY
# ==========================================

print("\n========== EDA SUMMARY ==========")

print("Total revenue:", round(df["Revenue"].sum(), 2))
print("Unique customers:", df["Customer ID"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique countries:", df["Country"].nunique())
print("Total invoices:", df["Invoice"].nunique())

print("\nEDA completed!")
print("Charts saved inside reports/figures/")
