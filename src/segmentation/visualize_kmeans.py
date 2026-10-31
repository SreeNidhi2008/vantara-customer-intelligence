import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print("Creating K-Means visualization...")

df = pd.read_csv("data/processed/kmeans_customer_segments.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Average_Basket_Size",
    "Customer_Lifetime_Days"
]

X = df[features].fillna(df[features].median())

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reduce to two dimensions
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)

df["PCA1"] = X_pca[:,0]
df["PCA2"] = X_pca[:,1]

os.makedirs("reports/figures", exist_ok=True)

plt.figure(figsize=(10,8))

for cluster in sorted(df["KMeans_Cluster"].unique()):
    subset = df[df["KMeans_Cluster"] == cluster]
    plt.scatter(
        subset["PCA1"],
        subset["PCA2"],
        s=30,
        alpha=0.7,
        label=f"Cluster {cluster}"
    )

plt.title("K-Means Customer Segmentation (PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.tight_layout()

plt.savefig(
    "reports/figures/kmeans_clusters_pca.png",
    dpi=300
)

plt.show()

print("\nPCA Explained Variance Ratio:")
print(pca.explained_variance_ratio_)
print("\nVisualization saved successfully!")
