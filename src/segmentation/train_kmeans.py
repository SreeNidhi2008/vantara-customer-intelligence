import pandas as pd
import os
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

print("Starting K-Means customer segmentation...")

# Load customer features
df = pd.read_csv("data/processed/customer_features.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Average_Basket_Size",
    "Customer_Lifetime_Days"
]

X = df[features].copy()

# Handle missing and infinite values
X = X.replace([float("inf"), float("-inf")], pd.NA)
X = X.fillna(X.median())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train K-Means with 5 clusters
model = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = model.fit_predict(X_scaled)

# Add cluster labels
df["KMeans_Cluster"] = clusters

# Evaluate clustering
score = silhouette_score(X_scaled, clusters)

print("\nK-Means Results")
print("----------------")
print("Number of customers:", len(df))
print("Number of clusters:", len(set(clusters)))
print("Silhouette Score:", round(score, 4))

print("\nCustomers in each cluster:")
print(df["KMeans_Cluster"].value_counts().sort_index())

# Save results and model
os.makedirs("models_artifacts", exist_ok=True)

df.to_csv("data/processed/kmeans_customer_segments.csv", index=False)

joblib.dump(model, "models_artifacts/kmeans_model.pkl")
joblib.dump(scaler, "models_artifacts/kmeans_scaler.pkl")

print("\nSaved customer clusters and model successfully!")
