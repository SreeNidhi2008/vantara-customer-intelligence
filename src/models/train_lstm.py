import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import joblib

df = pd.read_csv("data/processed/cleaned_retail_data.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Build monthly purchase sequences for each customer
monthly = (
    df.groupby(["Customer ID", pd.Grouper(key="InvoiceDate", freq="ME")])["Revenue"]
    .sum()
    .reset_index()
)

sequences = []

for _, group in monthly.groupby("Customer ID"):
    values = group["Revenue"].to_numpy(dtype=float)

    if len(values) >= 7:
        for i in range(len(values) - 6):
            sequences.append(values[i:i + 6])

if len(sequences) == 0:
    raise ValueError("Not enough purchase history to create sequences.")

X = np.array(sequences)
X = np.log1p(X)

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X.reshape(-1, 1)).reshape(X.shape)

X_train, X_test = train_test_split(
    X_scaled, test_size=0.2, random_state=42
)

# Predict the next month's purchase value
y_train = X_train[:, -1]
y_test = X_test[:, -1]

X_train = X_train[:, :-1].reshape(-1, 5, 1)
X_test = X_test[:, :-1].reshape(-1, 5, 1)

model = Sequential([
    LSTM(32, input_shape=(5, 1)),
    Dropout(0.2),
    Dense(16, activation="relu"),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

loss, mae = model.evaluate(X_test, y_test, verbose=0)

model.save("models_artifacts/lstm_purchase_model.keras")
joblib.dump(scaler, "models_artifacts/lstm_scaler.pkl")

print("LSTM training completed!")
print("Test MAE (scaled log revenue):", round(float(mae), 4))
print("Model saved successfully.")
