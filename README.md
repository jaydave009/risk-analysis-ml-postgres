# Risk Analysis ML Pipeline with PostgreSQL

##  Project Overview

This project is an end-to-end **Machine Learning pipeline** that predicts high-risk customers for financial institutions using historical account and transaction data. The pipeline integrates directly with **PostgreSQL**, making it production-ready.

- **Input:** Customer, account, and transaction data from PostgreSQL
- **Processing:** Feature engineering, encoding, scaling
- **Model:** Logistic Regression (predicts high-risk customers)
- **Output:** Predictions stored back in PostgreSQL and CSV files

---

## Tech Stack

- **Language:** Python 3.11  
- **Libraries:** pandas, scikit-learn, joblib, psycopg2, SQLAlchemy  
- **Database:** PostgreSQL  
- **Version Control:** Git & GitHub

---

## Database Schema

**customers table**

| Column       | Type    | Description                  |
|-------------|--------|------------------------------|
| customer_id | INT    | Unique ID for customer       |
| age         | INT    | Customer age                 |
| city        | TEXT   | Customer city                |
| account_type| TEXT   | Account type (savings/checking)|

**accounts table**

| Column       | Type    | Description                  |
|-------------|--------|------------------------------|
| account_id  | INT    | Unique ID for account        |
| customer_id | INT    | Linked customer ID           |
| balance     | FLOAT  | Current balance              |
| risk_score  | FLOAT  | Original risk score          |

**transactions table**

| Column         | Type    | Description                 |
|----------------|--------|-----------------------------|
| transaction_id | INT    | Unique ID for transaction   |
| customer_id    | INT    | Linked customer ID          |
| amount         | FLOAT  | Transaction amount          |
| transaction_date | DATE | Date of transaction         |
| category       | TEXT   | Transaction category        |

**predictions table** (created by pipeline)

| Column                 | Type  | Description                     |
|------------------------|-------|---------------------------------|
| customer_id            | INT   | Customer ID                     |
| high_risk_prediction   | INT   | 1 = High Risk, 0 = Low Risk     |

---

##  Pipeline Flow

```text
PostgreSQL (customers, accounts, transactions)
          │
          ▼
   Fetch & Feature Engineering
          │
          ▼
   Logistic Regression Model
          │
          ▼
Predictions stored back in PostgreSQL

