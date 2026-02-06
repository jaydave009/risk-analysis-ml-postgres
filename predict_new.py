# predict_new.py
from joblib import load
import numpy as np

# --- 1. Load the trained model ---
model = load('high_risk_model.joblib')
print("Model loaded successfully!\n")

# --- 2. Define new customer data ---
# Replace these values with actual customer features:
# [age, city_encoded, account_type_encoded, balance, total_transaction, avg_transaction, transaction_count]
# Note: Make sure the order and encoding match your training dataset
new_customers = np.array([
    [30, 1, 0, 20000, 500, 250, 2],
    [45, 0, 1, 60000, 1000, 1000, 1]
])

# --- 3. Predict high-risk labels ---
predictions = model.predict(new_customers)

# --- 4. Display results ---
for i, pred in enumerate(predictions, start=1):
    label = "High Risk" if pred == 1 else "Low Risk"
    print(f"Customer {i}: Predicted label = {pred} ({label})")
