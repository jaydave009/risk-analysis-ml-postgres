-- Create database (optional)
-- CREATE DATABASE risk_analysis_db;
## PostgreSQL Setup

1. Install PostgreSQL if not already installed: https://www.postgresql.org/download/
2. Open psql or PgAdmin.
3. Create a database (optional):
```sql
CREATE DATABASE risk_analysis_db;
\c risk_analysis_db
  
##  Create Tables
-- Table 1: customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    age INT NOT NULL,
    city TEXT NOT NULL,
    account_type TEXT NOT NULL
);

-- Table 2: accounts
CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    balance NUMERIC NOT NULL,
    risk_score NUMERIC NOT NULL
);

-- Table 3: transactions
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    amount NUMERIC NOT NULL,
    transaction_date DATE NOT NULL,
    category TEXT NOT NULL
);

-- Sample data (optional)
INSERT INTO customers (age, city, account_type) VALUES
(28, 'New York', 'savings'),
(35, 'Los Angeles', 'checking'),
(42, 'Chicago', 'savings'),
(30, 'Houston', 'checking'),
(50, 'Phoenix', 'savings');

INSERT INTO accounts (customer_id, balance, risk_score) VALUES
(1, 15000, 0.3),
(2, 50000, 0.8),
(3, 20000, 0.6),
(4, 70000, 0.9),
(5, 12000, 0.2);

INSERT INTO transactions (customer_id, amount, transaction_date, category) VALUES
(1, 200, '2026-01-10', 'grocery'),
(1, 500, '2026-01-12', 'utilities'),
(2, 1000, '2026-01-15', 'rent'),
(3, 150, '2026-01-20', 'grocery'),
(4, 2000, '2026-01-25', 'rent'),
(5, 100, '2026-01-28', 'grocery');
  
## Run the schema file
  psql -U your_username -d risk_analysis_db -f postgres_schema.sql


