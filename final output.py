from decimal import Decimal
import pandas as pd
from datetime import datetime

# ----------------------------
# Sample data (from your current merged dataset)
# ----------------------------
data = [
    [1, 28, 'New York', 'savings', 101, Decimal('15000'), Decimal('0.3'),
     [Decimal('200'), Decimal('500')]],  # customer 1 transactions
    [2, 35, 'Los Angeles', 'checking', 102, Decimal('50000'), Decimal('0.8'),
     [Decimal('1000')]],
    [3, 42, 'Chicago', 'savings', 103, Decimal('20000'), Decimal('0.6'),
     [Decimal('150')]],
    [4, 30, 'Houston', 'checking', 104, Decimal('70000'), Decimal('0.9'),
     [Decimal('2000')]],
    [5, 50, 'Phoenix', 'savings', 105, Decimal('12000'), Decimal('0.2'),
     []]  # no transactions
]

columns = ['customer_id', 'age', 'city', 'account_type', 'account_id', 'balance', 'risk_score', 'transactions']

df = pd.DataFrame(data, columns=columns)

# ----------------------------
# Feature Engineering
# ----------------------------
df['total_transactions'] = df['transactions'].apply(lambda x: sum(x) if x else Decimal('0'))
df['num_transactions'] = df['transactions'].apply(lambda x: len(x))
df['avg_transaction'] = df.apply(lambda row: row['total_transactions']/row['num_transactions'] 
                                 if row['num_transactions'] > 0 else Decimal('0'), axis=1)

# Optional: risk label based on balance and risk_score
def risk_label(row):
    if row['risk_score'] > 0.7 or row['balance'] < 10000:
        return 'High'
    elif row['risk_score'] > 0.4:
        return 'Medium'
    else:
        return 'Low'

df['risk_label'] = df.apply(risk_label, axis=1)

# ----------------------------
# Save final dataset
# ----------------------------
df_final = df.drop(columns=['transactions'])  # drop raw list of transactions if not needed
df_final.to_csv('customer_features.csv', index=False)

# ----------------------------
# Quick view
# ----------------------------
print("Final customer features:")
print(df_final)
