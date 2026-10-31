import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
import os

print("Starting SHAP explainability analysis...")

# Load churn dataset
df = pd.read_csv("data/processed/churn_dataset.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Customer_Lifetime_Days"
]

X = df[features]

# Use the same train/test split as the XGBoost model
from sklearn.model_selection import train_test_split

y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load trained XGBoost model
model = joblib.load("models_artifacts/xgboost_churn.pkl")

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Explain a sample of test customers
X_sample = X_test.sample(
    n=min(500, len(X_test)),
    random_state=42
)

shap_values = explainer.shap_values(X_sample)

os.makedirs("reports/figures", exist_ok=True)

# Global feature importance
plt.figure()
shap.summary_plot(
    shap_values,
    X_sample,
    show=False
)
plt.tight_layout()
plt.savefig(
    "reports/figures/shap_summary.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Feature importance bar chart
plt.figure()
shap.summary_plot(
    shap_values,
    X_sample,
    plot_type="bar",
    show=False
)
plt.tight_layout()
plt.savefig(
    "reports/figures/shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nSHAP analysis completed!")
print("Saved:")
print("- reports/figures/shap_summary.png")
print("- reports/figures/shap_feature_importance.png")
