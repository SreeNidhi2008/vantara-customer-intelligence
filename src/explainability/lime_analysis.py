import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

from lime.lime_tabular import LimeTabularExplainer
from sklearn.model_selection import train_test_split

print("Starting LIME explainability analysis...")

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
y = df["Churn"]

# Recreate training split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load XGBoost model
model = joblib.load("models_artifacts/xgboost_churn.pkl")

# Create LIME explainer
explainer = LimeTabularExplainer(
    training_data=X_train.to_numpy(),
    feature_names=features,
    class_names=["Active", "Churned"],
    mode="classification",
    discretize_continuous=True,
    random_state=42
)

# Explain one test customer
customer = X_test.iloc[0].to_numpy()

explanation = explainer.explain_instance(
    data_row=customer,
    predict_fn=model.predict_proba,
    num_features=len(features)
)

# Save explanation chart
os.makedirs("reports/figures", exist_ok=True)

fig = explanation.as_pyplot_figure()
fig.tight_layout()
fig.savefig(
    "reports/figures/lime_customer_explanation.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close(fig)

print("\nCustomer prediction:", 
      "Churned" if model.predict([customer])[0] == 1 else "Active")

print("\nLIME explanation:")
for feature, weight in explanation.as_list():
    print(f"{feature}: {weight:.4f}")

print("\nSaved: reports/figures/lime_customer_explanation.png")
print("LIME analysis completed!")
