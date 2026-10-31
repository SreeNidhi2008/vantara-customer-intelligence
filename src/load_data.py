
import pandas as pd
import os

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = "data/raw/online_retail_II.xlsx"

print("Loading dataset...")

sheets = pd.read_excel(file_path, sheet_name=None)
df = pd.concat(sheets.values(), ignore_index=True)

print("\nOriginal dataset shape:", df.shape)

# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\nStarting data cleaning...")

# Remove exact duplicate rows
df = df.drop_duplicates()

# Remove records with missing Customer IDs
df = df.dropna(subset=["Customer ID"])

# Remove records with missing descriptions
df = df.dropna(subset=["Description"])

# Remove cancelled invoices
df = df[~df["Invoice"].astype(str).str.startswith("C")]

# Keep only positive quantities
df = df[df["Quantity"] > 0]

# Keep only positive prices
df = df[df["Price"] > 0]

# ==========================================
# 3. FORMAT DATA TYPES
# ==========================================

df["Customer ID"] = df["Customer ID"].astype(int)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Description"] = df["Description"].str.strip()

# ==========================================
# 4. CREATE REVENUE COLUMN
# ==========================================

df["Revenue"] = df["Quantity"] * df["Price"]

# ==========================================
# 5. SAVE CLEANED DATASET
# ==========================================

os.makedirs("data/processed", exist_ok=True)

output_path = "data/processed/cleaned_retail_data.csv"

df.to_csv(output_path, index=False)

# ==========================================
# 6. CLEANING REPORT
# ==========================================

print("\n========== CLEANING REPORT ==========")

print("Original records: 1,067,371")
print("Cleaned records:", len(df))
print("Records removed:", 1067371 - len(df))

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nRemaining duplicate records:")
print(df.duplicated().sum())

print("\nUnique customers:", df["Customer ID"].nunique())

print("\nTotal revenue:", round(df["Revenue"].sum(), 2))

print("\nCleaned dataset saved successfully!")
print("Location:", output_path)

print("\n========== CLEANING COMPLETED ==========")
