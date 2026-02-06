# ML Risk Analysis with PostgreSQL Integration

## Project Overview
This project implements a **Machine Learning pipeline** to predict **high-risk customers** based on their account and transaction data.  
It fetches data directly from **PostgreSQL**, performs feature engineering, trains a model, and saves predictions back to the database.  

**Key Highlights:**
- End-to-end ML pipeline integrated with PostgreSQL
- Automated feature engineering
- Logistic Regression / Random Forest model
- Predictions stored in PostgreSQL and CSV
- Ready for new customer data

---

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/jaydave009/risk-analysis-ml-postgres.git
   cd risk-analysis-ml-postgres
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # Linux/Mac 
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
6.  Ensure PostgreSQL is running and the tables below exist:
    ```bash
    customers,accounts,transactions
    
## How to Run
Step 1 – Fetch & Process Features
         
                  python fetch_features.py
                  python db_feature_engineering.py

Step 2 – Train ML Model

                 python ml_model.py

Step 3 – Make Predictions

                  python run_risk_analysis.py
                  
Note : Predictions are saved in PostgreSQL and predictions.csv.


## ML Pipeline Flow 
          +-----------------+
        | Fetch Data      | <- PostgreSQL
        +-----------------+
                 |
                 v
        +-----------------+
        | Feature Engg    | <- Encode, aggregate transactions
        +-----------------+
                 |
                 v
        +-----------------+
        | Split Features  | <- X / y
        +-----------------+
                 |
                 v
        +-----------------+
        | Train Model     | <- Logistic Regression / Random Forest
        +-----------------+
                 |
                 v
        +-----------------+
        | Save Model/Scaler
        +-----------------+
                 |
                 v
        +-----------------+
        | Predict New Data| <- run_risk_analysis.py
        +-----------------+
                 |
                 v
        +-----------------+
        | Save Predictions| <- PostgreSQL & CSV
        +-----------------+
## File Structure 
```graphql
fetch_features.py         # Fetches data from PostgreSQL
db_feature_engineering.py # Feature engineering
ml_model.py               # Train and save ML model
run_risk_analysis.py      # Make predictions on new customers
save_predictions.py       # Store predictions in PostgreSQL
*.joblib                  # Saved model/scaler/training columns
new_customers.csv         # Optional CSV input
predictions.csv           # Output predictions
README.md                 # Project explanation

