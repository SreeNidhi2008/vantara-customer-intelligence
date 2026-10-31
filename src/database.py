import os
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:YOUR_PASSWORD@localhost:5432/vantara_db"
)

engine = create_engine(DATABASE_URL)

def save_customer_data():
    df = pd.read_csv("data/processed/customer_features.csv")

    df.to_sql(
        "customer_features",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Uploaded {len(df)} customer records to PostgreSQL.")

def check_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("PostgreSQL connected!")
        print(result.scalar())

if __name__ == "__main__":
    check_connection()
    save_customer_data()
