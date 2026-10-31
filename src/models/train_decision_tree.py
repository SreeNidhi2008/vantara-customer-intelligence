import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

print("Training Decision Tree churn model...")

df = pd.read_csv("data/processed/churn_dataset.csv")

X = df.drop(columns=["Customer ID", "Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(
    max_depth=8,
    min_samples_split=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nDECISION TREE PERFORMANCE")
print("-------------------------")
print("Accuracy:", round(accuracy_score(y_test, predictions), 4))
print("Precision:", round(precision_score(y_test, predictions), 4))
print("Recall:", round(recall_score(y_test, predictions), 4))
print("F1 Score:", round(f1_score(y_test, predictions), 4))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

os.makedirs("models_artifacts", exist_ok=True)

joblib.dump(
    model,
    "models_artifacts/decision_tree_churn.pkl"
)

print("\nDecision Tree model saved successfully!")
