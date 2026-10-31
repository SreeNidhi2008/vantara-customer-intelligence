import pandas as pd

data = {
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "Decision Tree",
        "XGBoost",
        "SVM",
        "ANN"
    ],
    "Accuracy": [0.7304, 0.7502, 0.7313, 0.7521, 0.7266, 0.7663],
    "Precision": [0.7561, 0.7738, 0.7430, 0.7530, 0.7866, 0.7713],
    "Recall": [0.7726, 0.7893, 0.8027, 0.8361, 0.7090, 0.8344],
    "F1 Score": [0.7643, 0.7815, 0.7717, 0.7924, 0.7458, 0.8016]
}

df = pd.DataFrame(data)
df = df.sort_values(by="F1 Score", ascending=False)

print("\nChurn Model Comparison")
print("----------------------")
print(df.to_string(index=False))

df.to_csv("reports/churn_model_comparison.csv", index=False)

print("\nBest Model:", df.iloc[0]["Model"])
print("Best F1 Score:", df.iloc[0]["F1 Score"])
print("\nComparison report updated!")
