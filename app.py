from flask import Flask, jsonify, render_template
from flask_cors import CORS
from ml_models import get_anomaly_predictions, get_phishing_predictions
import config
import pymongo
from bson import json_util
import json
import datetime # We'll need this for the agent

# --- Database Setup ---
client = pymongo.MongoClient(config.MONGO_URI)
db = client.cyber_db
alerts_collection = db.alerts
blocklist_collection = db.blocklist # <-- NEW: Collection for our blocklist

# --- App Setup ---
app = Flask(__name__)
CORS(app)

# ===================================================================
# --- NEW: AI Agent Function ---
# ===================================================================
def trigger_agent_response(alert):
    """
    This function acts as our "AI Agent".
    It takes an alert and performs an action.
    """
    print(f"AI AGENT: High-level threat detected: {alert['threat']}")
    
    # 1. Determine what to block (IP or Email Source)
    identifier_to_block = None
    block_type = None
    
    if 'ip' in alert and alert['ip'] != 'N/A':
        identifier_to_block = alert['ip']
        block_type = 'ip'
    elif 'source' in alert:
        identifier_to_block = alert['source']
        block_type = 'email_source'
    
    # 2. If we have something to block, add it to the blocklist
    if identifier_to_block:
        # We use 'update_one' with 'upsert=True'
        # This acts as a "add if it doesn't exist" command,
        # preventing duplicate entries.
        blocklist_collection.update_one(
            {'identifier': identifier_to_block}, # The filter to find
            {
                '$set': { # The data to write
                    'identifier': identifier_to_block,
                    'type': block_type,
                    'reason': alert['threat'],
                    'blocked_on': datetime.datetime.now(datetime.timezone.utc)
                }
            },
            upsert=True # This is the magic "insert if not found"
        )
        print(f"AI AGENT: Action taken - Added '{identifier_to_block}' to blocklist.")
    else:
        print("AI AGENT: No specific IP/Source to block.")

# ===================================================================

@app.route("/")
def home():
    return render_template("index.html")

# --- UPDATED API Endpoint for Alerts ---
@app.route("/api/get_alerts")
def get_alerts():
    # 1. Run the ML models
    anomaly_alerts = get_anomaly_predictions()
    phishing_alerts = get_phishing_predictions()
    new_alerts = anomaly_alerts + phishing_alerts
    
    # 2. If new alerts were found...
    if new_alerts:
        try:
            # 2a. Save them to the DB
            alerts_collection.insert_many(new_alerts)
            print(f"Inserted {len(new_alerts)} new alerts into DB.")
            
            # 2b. <-- NEW: Trigger AI Agent for high-level threats
            for alert in new_alerts:
                if alert.get('level') == 'High':
                    trigger_agent_response(alert)
                    
        except Exception as e:
            print(f"Error during alert processing: {e}")

    # 3. Fetch ALL alerts from the database
    all_alerts_cursor = alerts_collection.find().sort("timestamp", -1).limit(20)
    alerts_list = json.loads(json_util.dumps(all_alerts_cursor))

    # 4. Send the list to the frontend
    return jsonify(alerts_list)

# --- NEW API Endpoint for the Blocklist ---
@app.route("/api/get_blocklist")
def get_blocklist():
    """
    A new API endpoint to let the dashboard see what's on the blocklist.
    """
    try:
        blocklist_cursor = blocklist_collection.find().sort("blocked_on", -1)
        blocklist = json.loads(json_util.dumps(blocklist_cursor))
        return jsonify(blocklist)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)