import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
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

input_layer = Input(shape=(X_scaled.shape[1],))
encoded = Dense(4, activation="relu")(input_layer)
encoded = Dense(2, activation="relu")(encoded)
decoded = Dense(4, activation="relu")(encoded)
output_layer = Dense(X_scaled.shape[1], activation="linear")(decoded)

autoencoder = Model(input_layer, output_layer)
autoencoder.compile(optimizer="adam", loss="mse")

autoencoder.fit(
    X_scaled,
    X_scaled,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    shuffle=True,
    verbose=1
)

reconstructed = autoencoder.predict(X_scaled, verbose=0)
errors = np.mean(np.square(X_scaled - reconstructed), axis=1)

threshold = np.percentile(errors, 95)

df["Anomaly_Score"] = errors
df["Is_Anomaly"] = (errors > threshold).astype(int)

autoencoder.save("models_artifacts/anomaly_autoencoder.keras")
joblib.dump(scaler, "models_artifacts/anomaly_scaler.pkl")
df.to_csv("data/processed/anomaly_results.csv", index=False)

print("Anomaly detection completed!")
print("Anomalies detected:", int(df["Is_Anomaly"].sum()))
print("Results saved to data/processed/anomaly_results.csv")
