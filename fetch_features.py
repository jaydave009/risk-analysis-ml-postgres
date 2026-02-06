# *******ABOVE ONE WAS AS PANDAS *****************

import pandas as pd
from sqlalchemy import create_engine

def fetch_feature_data():

    engine = create_engine(
        "postgresql+psycopg2://postgres:mirai%40703@localhost:5432/finance_analytics"
    )

    query = """
    SELECT 
        c.customer_id,
        c.age,
        c.city,
        c.account_type,
        a.balance,
        a.risk_score,
        SUM(t.amount) AS total_transaction,
        AVG(t.amount) AS avg_transaction,
        COUNT(t.amount) AS transaction_count
    FROM customers c
    JOIN accounts a ON c.customer_id = a.customer_id
    LEFT JOIN transactions t ON c.customer_id = t.customer_id
    GROUP BY c.customer_id, a.balance, a.risk_score
    ORDER BY c.customer_id;
    """

    df = pd.read_sql(query, engine)

    return df


if __name__ == "__main__":
    df = fetch_feature_data()
    print("Fetched dataset:")
    print(df)
