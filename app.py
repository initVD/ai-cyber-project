from flask import Flask, jsonify, render_template  # Import render_template
from flask_cors import CORS  # Import CORS

# 1. Create the app
app = Flask(__name__)

# 2. Setup CORS
# This tells the browser to allow your frontend (on the same machine)
# to request data from your backend.
CORS(app)

# 3. Update your homepage route
# Now, this route will serve your HTML file
@app.route("/")
def home():
    # render_template looks in your 'templates' folder
    # and sends 'index.html' to the browser.
    return render_template("index.html")

# 4. Your API endpoint
@app.route("/api/get_alerts")
def get_alerts():
    dummy_alerts = [
        {"id": 1, "threat": "Phishing Attempt", "ip": "192.168.1.10", "level": "High"},
        {"id": 2, "threat": "Suspicious Login", "ip": "10.0.0.5", "level": "Medium"},
        {"id": 3, "threat": "Anomaly Detected", "ip": "203.0.113.45", "level": "Low"}
    ]
    return jsonify(dummy_alerts)

# 5. Run the app
if __name__ == "__main__":
    app.run(debug=True)