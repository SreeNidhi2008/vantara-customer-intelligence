import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/processed/churn_dataset.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Customer_Lifetime_Days"
]

X = df[features].fillna(df[features].median())
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = joblib.load("models_artifacts/xgboost_churn.pkl")

fig, ax = plt.subplots(figsize=(12, 8))

PartialDependenceDisplay.from_estimator(
    model,
    X_test,
    features=features,
    kind="average",
    ax=ax
)

plt.tight_layout()
plt.savefig(
    "reports/figures/partial_dependence.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("Partial dependence analysis completed!")
print("Chart saved to reports/figures/partial_dependence.png")
