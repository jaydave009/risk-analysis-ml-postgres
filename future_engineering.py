import numpy as np
import pandas as pd

# Example mock data (replace with actual data)
customers = np.array([
    [1, 28, 'CityA', 'Savings'],
    [2, 35, 'CityB', 'Current'],
    [3, 42, 'CityC', 'Savings'],
    [4, 30, 'CityD', 'Current'],
    [5, 50, 'CityE', 'Savings']
])

accounts = np.array([
    [1, 1, 15000, 0.5],
    [2, 2, 50000, 0.8],
    [3, 3, 20000, 0.3],
    [4, 4, 70000, 0.9],
    [5, 5, 12000, 0.4]
])

transactions = np.array([
    [1, 1, 700],
    [2, 1, 350],
    [3, 2, 1000],
    [4, 2, 1000],
    [5, 3, 150],
    [6, 3, 150],
    [7, 4, 2000],
    [8, 4, 2000]
])

# --- 1. Risk label ---
risk_score = accounts[:, 3].astype(float)
high_risk = np.where(risk_score > 0.7, 1, 0)

# --- 2. Transaction aggregates ---
customer_ids = customers[:, 0]
total_transaction, avg_transaction, transaction_count = [], [], []

for cid in customer_ids:
    cust_tx = transactions[transactions[:,1].astype(int) == int(cid)][:,2].astype(float)
    total_transaction.append(np.sum(cust_tx))
    avg_transaction.append(np.mean(cust_tx) if len(cust_tx) > 0 else 0)
    transaction_count.append(len(cust_tx))

# --- 3. Encode categorical variables ---
cities = list(set(customers[:,2]))
city_encoded = np.array([cities.index(c) for c in customers[:,2]])

account_types = list(set(customers[:,3]))
account_type_encoded = np.array([account_types.index(a) for a in customers[:,3]])

# --- 4. Merge all features into DataFrame ---
balances = accounts[:,2].astype(float)

training_columns = [
    'age', 'city_encoded', 'account_type_encoded', 'balance', 
    'total_transaction', 'avg_transaction', 'transaction_count'
]

final_dataset = pd.DataFrame({
    'age': customers[:,1].astype(float),
    'city_encoded': city_encoded,
    'account_type_encoded': account_type_encoded,
    'balance': balances,
    'total_transaction': total_transaction,
    'avg_transaction': avg_transaction,
    'transaction_count': transaction_count,
    'target': high_risk
})

print("Final dataset shape:", final_dataset.shape)
