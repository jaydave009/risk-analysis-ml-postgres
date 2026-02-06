# Final_output.py
# Complete working script

import pandas as pd
from decimal import Decimal
import datetime

# -----------------------------
# 1. Raw Data
# -----------------------------

customers = [
    ['1', '28', 'New York', 'savings'],
    ['2', '35', 'Los Angeles', 'checking'],
    ['3', '42', 'Chicago', 'savings'],
    ['4', '30', 'Houston', 'checking'],
    ['5', '50', 'Phoenix', 'savings']
]

accounts = [
    [101, 1, Decimal('15000'), Decimal('0.3')],
    [102, 2, Decimal('50000'), Decimal('0.8')],
    [103, 3, Decimal('20000'), Decimal('0.6')],
    [104, 4, Decimal('70000'), Decimal('0.9')],
    [105, 5, Decimal('12000'), Decimal('0.2')]
]

transactions = [
    [1001, 1, Decimal('200'), datetime.datetime(2026, 1, 10), 'grocery'],
    [1002, 1, Decimal('500'), datetime.datetime(2026, 1, 12), 'utilities'],
    [1003, 2, Decimal('1000'), datetime.datetime(2026, 1, 15), 'rent'],
    [1004, 3, Decimal('150'), datetime.datetime(2026, 1, 20), 'grocery'],
    [1005, 4, Decimal('2000'), datetime.datetime(2026, 1, 25), 'rent']
]

# -----------------------------
# 2. Convert to DataFrames
# -----------------------------
df_customers = pd.DataFrame(customers, columns=['customer_id', 'age', 'city', 'account_type'])
df_customers['customer_id'] = df_customers['customer_id'].astype(int)
df_customers['age'] = df_customers['age'].astype(int)

df_accounts = pd.DataFrame(accounts, columns=['account_id', 'customer_id', 'balance', 'risk_score'])
df_transactions = pd.DataFrame(transactions, columns=['transaction_id', 'customer_id', 'amount', 'date', 'category'])

# -----------------------------
# 3. Aggregate Transactions
# -----------------------------
# Total and average transaction per customer
agg_transactions = df_transactions.groupby('customer_id')['amount'].agg(
    total_transactions='sum',
    num_transactions='count'
).reset_index()

agg_transactions['avg_transaction'] = agg_transactions.apply(
    lambda x: x['total_transactions'] / x['num_transactions'], axis=1
)

# -----------------------------
# 4. Merge all into final dataframe
# -----------------------------
final_customer_df = pd.merge(df_customers, df_accounts, on='customer_id', how='left')
final_customer_df = pd.merge(final_customer_df, agg_transactions, on='customer_id', how='left')

# Fill NaN for customers with no transactions
final_customer_df[['total_transactions', 'num_transactions', 'avg_transaction']] = \
    final_customer_df[['total_transactions', 'num_transactions', 'avg_transaction']].fillna(0)

# -----------------------------
# 5. Assign Risk Labels
# -----------------------------
def risk_label(row):
    if row['risk_score'] <= 0.3:
        return 'Low'
    elif row['risk_score'] <= 0.7:
        return 'Medium'
    else:
        return 'High'

final_customer_df['risk_label'] = final_customer_df.apply(risk_label, axis=1)

# -----------------------------
# 6. Final Output
# -----------------------------
print("Final Customer Features:\n")
print(final_customer_df)
