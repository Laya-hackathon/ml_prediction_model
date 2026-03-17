import os
import pandas as pd
import joblib
import json

from utils import model_predict, send_to_agent

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
_CODE_DIR = os.path.join(_SCRIPTS_DIR, "..")

# Load model
model = joblib.load(os.path.join(_CODE_DIR, "model_and_setting", "xgb_v0.pkl"))

# Load feature columns
with open(os.path.join(_CODE_DIR, "model_and_setting", "feature_columns.json")) as f:
    feature_columns = json.load(f)

print("Model and feature columns loaded successfully.")

# Load test data
test_users_df = pd.read_csv(os.path.join(_CODE_DIR, "data", "test_users_data.csv"))
print("Test users data loaded successfully.")

# Ensure correct feature order
new_data = test_users_df[feature_columns]

# Take ONE input
input_df = new_data.iloc[[0]]
print(input_df.head())
user_id = test_users_df["member_id"].iloc[0]
claim_id = test_users_df["claim_id"].iloc[0]

print(input_df)

# Predict
prediction, probability = model_predict(input_df, model)

# Send result
send_to_agent(prediction, probability, user_id, claim_id)