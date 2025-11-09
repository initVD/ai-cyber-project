import pandas as pd
from sklearn.ensemble import IsolationForest
import random

# --- Part 1: Simulate Your Training Data ---
# In a real project, this data would come from a huge log file or database.
# For now, we'll create a simple 'dummy' dataset.
# We're simulating log data: 'login_attempts', 'failed_attempts', 'session_duration'
data = {
    'login_attempts': [1, 2, 1, 3, 2, 1, 4, 1, 2, 5, 1, 2, 3, 1, 2, 100], # Normal users + 1 anomaly
    'failed_attempts': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 50], # Normal users + 1 anomaly
    'session_duration': [10, 12, 15, 8, 11, 14, 20, 9, 13, 25, 11, 10, 16, 12, 10, 1] # Normal users + 1 anomaly
}
# The 'anomaly' (last row) is a user with 100 logins, 50 failures, and a 1-second session
# This is a classic 'brute force' attack pattern.

# Convert our data into a 'DataFrame', which is what pandas uses
df = pd.DataFrame(data)

# --- Part 2: Train the AI Model ---
print("Training Anomaly Detection model...")

# 1. Create the model: IsolationForest
# 'contamination=0.1' means we 'expect' about 10% of our data to be anomalies
model = IsolationForest(contamination=0.1, random_state=42)

# 2. 'Train' the model on our data
# The model learns what 'normal' behavior looks like.
model.fit(df)

print("Model trained.")

# --- Part 3: Create a Function to Get Predictions ---
# This is the function our 'app.py' server will call.

def get_anomaly_predictions():
    print("Generating new 'live' data and checking for anomalies...")
    
    # 1. Simulate new, incoming "live" log data
    # We'll create 5 new 'log events' to check
    new_logs = []
    for _ in range(5):
        # Most logs will be 'normal'
        log = {
            'ip': f"192.168.1.{random.randint(10, 100)}",
            'login_attempts': random.randint(1, 5),
            'failed_attempts': random.randint(0, 2),
            'session_duration': random.randint(5, 30)
        }
        new_logs.append(log)

    # 2. Add one 'obvious' anomaly to our new logs for testing
    anomaly_log = {
        'ip': '203.0.113.99', # A suspicious IP
        'login_attempts': 150,
        'failed_attempts': 75,
        'session_duration': 2
    }
    new_logs.append(anomaly_log)

    # 3. Convert our new logs into a DataFrame for the model
    live_df = pd.DataFrame(new_logs)
    
    # 4. Use the model to 'predict' anomalies
    # The model will check the 'login_attempts', 'failed_attempts', and 'session_duration'
    # It will output:
    #  1 for 'normal' (inlier)
    # -1 for 'anomalous' (outlier)
    predictions = model.predict(live_df[['login_attempts', 'failed_attempts', 'session_duration']])
    
    # 5. Format the results to send to our dashboard
    alerts_list = []
    
    for index, log in enumerate(new_logs):
        if predictions[index] == -1: # If the model flagged it as an anomaly
            alert = {
                "id": index + 1,
                "threat": "Anomaly Detected (Suspicious Login Pattern)",
                "ip": log['ip'],
                "level": "High",
                "details": f"Logins: {log['login_attempts']}, Fails: {log['failed_attempts']}, Duration: {log['session_duration']}s"
            }
            alerts_list.append(alert)
            
    return alerts_list

# --- Part 4: Test the function (optional) ---
# You can 'uncomment' the lines below to test this file directly
# if __name__ == "__main__":
#     alerts = get_anomaly_predictions()
#     print("\n--- Generated Alerts ---")
#     print(alerts)