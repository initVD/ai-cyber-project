from flask import Flask, jsonify, render_template
from flask_cors import CORS
# Import BOTH model functions
from ml_models import get_anomaly_predictions, get_phishing_predictions
import config
import pymongo
from bson import json_util # Needed to handle MongoDB's _id
import json

# --- Database Setup ---
client = pymongo.MongoClient(config.MONGO_URI)
db = client.cyber_db
alerts_collection = db.alerts

# --- App Setup ---
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

# --- UPDATED API ENDPOINT ---
@app.route("/api/get_alerts")
def get_alerts():
    # 1. Run the ML models to get new, "live" alerts
    anomaly_alerts = get_anomaly_predictions()
    phishing_alerts = get_phishing_predictions()
    
    # Combine the alerts from both models
    new_alerts = anomaly_alerts + phishing_alerts
    
    # 2. If any new alerts were found, save them to the database
    if new_alerts:
        try:
            alerts_collection.insert_many(new_alerts)
            print(f"Inserted {len(new_alerts)} new alerts into DB.")
        except Exception as e:
            print(f"Error inserting into DB: {e}")

    # 3. Fetch ALL alerts from the database to show on the dashboard
    all_alerts_cursor = alerts_collection.find().sort("timestamp", -1).limit(20)
    
    # 4. Convert the cursor to a JSON-friendly list
    alerts_list = json.loads(json_util.dumps(all_alerts_cursor))

    # 5. Send the full list of historical alerts to the frontend
    return jsonify(alerts_list)

if __name__ == "__main__":
    app.run(debug=True)