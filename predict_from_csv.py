# predict_from_csv.py
import pandas as pd
from joblib import load

# --- 1. Load the trained model ---
model = load('high_risk_model.joblib')
print("Model loaded successfully!\n")

# --- 2. Read new customers from CSV ---
df_new = pd.read_excel('new_customers.xlsx')
print("New customer data loaded:")
print(df_new, "\n")

# --- 3. Predict ---
predictions = model.predict(df_new.values)

# --- 4. Add predictions to DataFrame ---
df_new['predicted_label'] = predictions
df_new['risk_label'] = df_new['predicted_label'].apply(lambda x: "High Risk" if x==1 else "Low Risk")

# --- 5. Show results ---
print("Predictions:")
print(df_new)

# --- 6. Optional: save predictions ---
df_new.to_csv('predictions.csv', index=False)
print("\nPredictions saved to 'predictions.csv'")
