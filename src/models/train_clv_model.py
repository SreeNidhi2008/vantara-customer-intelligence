import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data/processed/clv_dataset.csv")

features = [
    "Recency",
    "Frequency",
    "Monetary",
    "Average_Order_Value",
    "Customer_Lifetime_Days"
]

X = df[features].fillna(df[features].median())
y = df["Future_90_Day_Revenue"].clip(lower=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = TransformedTargetRegressor(
    regressor=RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        min_samples_leaf=3,
        random_state=42,
        n_jobs=-1
    ),
    func=np.log1p,
    inverse_func=np.expm1
)

model.fit(X_train, y_train)
predictions = np.maximum(model.predict(X_test), 0)

baseline = DummyRegressor(strategy="median")
baseline.fit(X_train, y_train)
baseline_predictions = baseline.predict(X_test)

print("\nCLV Model Performance")
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 2))
print("R2:", round(r2_score(y_test, predictions), 4))

print("\nBaseline Performance")
print("Baseline MAE:", round(mean_absolute_error(y_test, baseline_predictions), 2))

joblib.dump(model, "models_artifacts/clv_random_forest.pkl")

print("\nImproved CLV model saved successfully!")
