# import pandas as pd
# import joblib

# # Load model, scaler, and training columns
# model = joblib.load('high_risk_model.joblib')
# scaler = joblib.load('scaler.joblib')
# training_columns = joblib.load('training_columns.joblib')
# print("Model, scaler, and training columns loaded successfully!")

# # Load new customer data (CSV with proper column names)
# new_data_file = 'new_customers.csv'  # make sure CSV headers match training_columns
# df_new = pd.read_csv(new_data_file)
# print("New customer data loaded:\n", df_new)

# # Align columns and order
# df_new_aligned = df_new[training_columns]  # must match training_columns exactly

# # Scale features
# X_new_scaled = scaler.transform(df_new_aligned)

# # Predict
# predictions = model.predict(X_new_scaled)
# df_new['high_risk_prediction'] = predictions

# # Save predictions
# df_new.to_csv('predictions.csv', index=False)
# print("Predictions saved to 'predictions.csv'")
# print(df_new)

# ******************ABOVE ONE FOR CSV TEST ***********************

import joblib
import pandas as pd
from fetch_features import fetch_feature_data

model = joblib.load("high_risk_model.joblib")
scaler = joblib.load("scaler.joblib")
training_columns = joblib.load("training_columns.joblib")

df_new = fetch_feature_data()

df_new["city_encoded"] = df_new["city"].astype("category").cat.codes
df_new["account_type_encoded"] = df_new["account_type"].astype("category").cat.codes

X_new = df_new[training_columns]

#VERY IMPORTANT LINE (FIX NaN)
X_new = X_new.fillna(0)

X_new_scaled = scaler.transform(X_new)

predictions = model.predict(X_new_scaled)

df_new["high_risk_prediction"] = predictions

df_new.to_csv("predictions.csv", index=False)

print(df_new[["customer_id", "high_risk_prediction"]])
print("Predictions saved!")
