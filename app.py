from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from ml_models import get_anomaly_predictions, get_phishing_predictions, get_fraud_login_predictions
import config
import pymongo
from bson import json_util
import json
import datetime

# --- NEW: Import JWT libraries ---
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# --- Database Setup ---
client = pymongo.MongoClient(config.MONGO_URI)
db = client.cyber_db
alerts_collection = db.alerts
blocklist_collection = db.blocklist

# --- App Setup ---
app = Flask(__name__)
CORS(app)

# --- NEW: Setup JWT Configuration ---
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
jwt = JWTManager(app)

# --- NEW: Create a hardcoded user database (for demo) ---
# In a real app, this would be in your database
DEMO_USERS = {
    "admin": "password123"
}

# ===================================================================
# --- AI Agent Function (Unchanged) ---
# ===================================================================
def trigger_agent_response(alert):
    print(f"AI AGENT: High-level threat detected: {alert['threat']}")
    identifier_to_block = None
    block_type = None
    
    if 'ip' in alert and alert['ip'] != 'N/A':
        identifier_to_block = alert['ip']
        block_type = 'ip'
    elif 'source' in alert:
        identifier_to_block = alert['source']
        block_type = 'email_source'
    
    if identifier_to_block:
        blocklist_collection.update_one(
            {'identifier': identifier_to_block},
            {'$set': {
                'identifier': identifier_to_block,
                'type': block_type,
                'reason': alert['threat'],
                'blocked_on': datetime.datetime.now(datetime.timezone.utc)
            }},
            upsert=True
        )
        print(f"AI AGENT: Action taken - Added '{identifier_to_block}' to blocklist.")
    else:
        print("AI AGENT: No specific IP/Source to block.")

# ===================================================================
# --- NEW: Login Routes ---
# ===================================================================

@app.route("/login")
def login_page():
    """Serves the login.html page."""
    return render_template("login.html")

@app.route("/api/login", methods=["POST"])
def api_login():
    """Handles the login POST request from login.js."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check against our hardcoded user
    if username in DEMO_USERS and DEMO_USERS[username] == password:
        # User is correct! Create a token.
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    # Bad credentials
    return jsonify({"msg": "Bad username or password"}), 401

# ===================================================================
# --- PROTECTED Dashboard Routes ---
# ===================================================================

@app.route("/")

def home():
    """Serves the main dashboard (index.html)."""
    # This route is now protected.
    # If no valid JWT, the user will be rejected (we'll handle redirect in JS)
    return render_template("index.html")

@app.route("/api/get_alerts")
@jwt_required() # <-- PROTECTED!
def get_alerts():
    """Gets all alerts. Protected route."""
    anomaly_alerts = get_anomaly_predictions()
    phishing_alerts = get_phishing_predictions()
    fraud_login_alerts = get_fraud_login_predictions()
    
    new_alerts = anomaly_alerts + phishing_alerts + fraud_login_alerts
    
    if new_alerts:
        try:
            alerts_collection.insert_many(new_alerts)
            print(f"Inserted {len(new_alerts)} new alerts into DB.")
            for alert in new_alerts:
                if alert.get('level') == 'High':
                    trigger_agent_response(alert)
        except Exception as e:
            print(f"Error during alert processing: {e}")

    all_alerts_cursor = alerts_collection.find().sort("timestamp", -1).limit(20)
    alerts_list = json.loads(json_util.dumps(all_alerts_cursor))
    return jsonify(alerts_list)

@app.route("/api/get_blocklist")
@jwt_required() # <-- PROTECTED!
def get_blocklist():
    """Gets the blocklist. Protected route."""
    try:
        blocklist_cursor = blocklist_collection.find().sort("blocked_on", -1)
        blocklist = json.loads(json_util.dumps(blocklist_cursor))
        return jsonify(blocklist)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)