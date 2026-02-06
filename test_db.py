import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="finance_analytics",
    user="postgres",
    password="mirai@703"
)

query = "SELECT * FROM customers;"
df = pd.read_sql(query, conn)

print(df)

conn.close()
