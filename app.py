from flask import Flask, jsonify, render_template
from flask_cors import CORS
from ml_models import get_anomaly_predictions  # <--- IMPORT YOUR NEW FUNCTION

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

# --- UPDATED API ENDPOINT ---
@app.route("/api/get_alerts")
def get_alerts():
    # Instead of dummy data, we now CALL our ML model!
    # Every time you refresh the page, the model will re-run
    # on new simulated data.
    alerts = get_anomaly_predictions() 
    
    # If no anomalies are found, send a different message
    if not alerts:
        return jsonify([
            {
                "id": 1,
                "threat": "System Nominal",
                "ip": "N/A",
                "level": "Low",
                "details": "No anomalies detected in the last scan."
            }
        ])
    
    return jsonify(alerts) # Send the real alerts

if __name__ == "__main__":
    app.run(debug=True)