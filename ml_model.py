# import joblib
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import cross_val_score
# from future_engineering import final_dataset, training_columns

# # Features and target
# X = final_dataset[training_columns]  # DataFrame keeps column names
# y = final_dataset['target']

# # Scale features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Train Logistic Regression
# model = LogisticRegression(max_iter=500)
# model.fit(X_scaled, y)

# # Cross-validation
# cv_scores = cross_val_score(model, X_scaled, y, cv=3)
# print("Cross-validated scores:", cv_scores)
# print("Mean CV accuracy:", cv_scores.mean())

# # Save model, scaler, and columns
# joblib.dump(model, 'high_risk_model.joblib')
# joblib.dump(scaler, 'scaler.joblib')
# joblib.dump(training_columns, 'training_columns.joblib')
# print("Model, scaler, and training columns saved successfully!")

# ******************************** ABOVE ONE FOR CSV _____________________________________
import joblib
from sklearn.ensemble import RandomForestClassifier

from fetch_features import fetch_feature_data
from db_feature_engineering import prepare_features

df = fetch_feature_data()
X, y = prepare_features(df)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "risk_model.pkl")

print("Model trained and saved!")
