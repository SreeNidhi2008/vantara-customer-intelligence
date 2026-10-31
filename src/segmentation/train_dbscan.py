import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import joblib

df = pd.read_csv("data/processed/customer_features.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Average_Basket_Size",
    "Customer_Lifetime_Days"
]

X = df[features].fillna(df[features].median())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = DBSCAN(eps=0.8, min_samples=10)
labels = model.fit_predict(X_scaled)

df["DBSCAN_Cluster"] = labels

clusters = set(labels) - {-1}
if len(clusters) >= 2:
    score = silhouette_score(
        X_scaled[labels != -1],
        labels[labels != -1]
    )
    print("Silhouette Score:", round(score, 4))
else:
    print("Not enough clusters for silhouette score.")

print("\nCluster Distribution:")
print(df["DBSCAN_Cluster"].value_counts().sort_index())

df.to_csv("data/processed/dbscan_customer_segments.csv", index=False)
joblib.dump(model, "models_artifacts/dbscan_model.pkl")
joblib.dump(scaler, "models_artifacts/dbscan_scaler.pkl")

print("\nDBSCAN segmentation completed!")
