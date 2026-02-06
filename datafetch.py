# step1_fetch_data.py
import psycopg2
import numpy as np

# 1. Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",        # your DB host
        database="finance_analytics", # your DB name
        user="postgres",     # your DB username
        password="mirai@703" # your DB password
    )
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Error connecting to PostgreSQL:", e)
    exit()

# 2. Create a function to fetch a table and convert to NumPy array
def fetch_table(table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    return np.array(rows)

# 3. Fetch the tables
customers = fetch_table("customers")
accounts = fetch_table("accounts")
transactions = fetch_table("transactions")

# 4. Print basic info
print("Customers table shape:", customers.shape)
print("Accounts table shape:", accounts.shape)
print("Transactions table shape:", transactions.shape)

print("\nFirst 5 customers:")
print(customers[:5])

print("\nFirst 5 accounts:")
print(accounts[:5])

print("\nFirst 5 transactions:")
print(transactions[:5])

# 5. Close connection
conn.close()
