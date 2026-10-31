import pandas as pd
import matplotlib.pyplot as plt
import os

print("Creating customer segment visualization...")

df = pd.read_csv("data/processed/customer_segments.csv")

segment_counts = df["Customer_Segment"].value_counts()

os.makedirs("reports/figures", exist_ok=True)

plt.figure(figsize=(10, 6))
segment_counts.plot(kind="bar")

plt.title("Customer Distribution by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig("reports/figures/customer_segments.png", dpi=300)
plt.show()

print("\nChart saved to reports/figures/customer_segments.png")
