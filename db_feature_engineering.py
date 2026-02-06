import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_features(df):

    # --------------------
    # Handle missing values (VERY IMPORTANT)
    # --------------------
    df = df.fillna(0)

    # --------------------
    # Create target from risk_score
    # --------------------
    df["high_risk"] = (df["risk_score"] > 0.7).astype(int)

    # --------------------
    # Encode categorical columns
    # --------------------
    le_city = LabelEncoder()
    le_account = LabelEncoder()

    df["city_encoded"] = le_city.fit_transform(df["city"])
    df["account_type_encoded"] = le_account.fit_transform(df["account_type"])

    # --------------------
    # Feature set
    # --------------------
    X = df[
        [
            "age",
            "city_encoded",
            "account_type_encoded",
            "balance",
            "total_transaction",
            "avg_transaction",
            "transaction_count",
        ]
    ]

    y = df["high_risk"]

    return X, y
