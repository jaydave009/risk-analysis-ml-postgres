import psycopg2
import pandas as pd
from fetch_features import fetch_feature_data
from db_feature_engineering import prepare_features
import joblib

def save_predictions_to_db():

    # Fetch data
    df = fetch_feature_data()

    # Prepare ML features
    X, _ = prepare_features(df)

    # Load trained model
    model = joblib.load("risk_model.pkl")

    # Predict
    predictions = model.predict(X)

    # Build result dataframe
    result_df = pd.DataFrame({
        "customer_id": df["customer_id"],
        "high_risk_prediction": predictions
    })

    # Connect to PostgreSQL
    conn = psycopg2.connect(
     host="localhost",
    database="finance_analytics",
    user="postgres",
    password="mirai@703"
    )

    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS risk_predictions (
            customer_id INT,
            high_risk_prediction INT,
            prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert predictions
    for _, row in result_df.iterrows():
        cur.execute(
            "INSERT INTO risk_predictions (customer_id, high_risk_prediction) VALUES (%s, %s)",
            (int(row["customer_id"]), int(row["high_risk_prediction"]))
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Predictions saved into PostgreSQL!")

if __name__ == "__main__":
    save_predictions_to_db()
