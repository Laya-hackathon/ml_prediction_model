import pickle, pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score
from sklearn.metrics import ConfusionMatrixDisplay



def model_predict(input_df, model):

    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    return prediction, probability

def send_to_agent(prediction, probability, user_id, claim_id):

    output = {
        "member_id": str(user_id),
        "claim_id": claim_id,
        "predicted_risk": prediction,
        "risk_probability": probability
    }

    import urllib.request
    SERVER_URL = "http://localhost:8000/api/ingest"

    try:
        body = json.dumps(output).encode("utf-8")
        req = urllib.request.Request(SERVER_URL, data=body, headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=10)
        print(f"Sent to server: {output}")
    except Exception as e:
        print(f"Could not reach server, saving locally instead. Error: {e}")
        with open("output.json", "w") as f:
            json.dump(output, f, indent=4)