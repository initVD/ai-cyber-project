import pandas as pd
from sklearn.ensemble import IsolationForest
import random
import datetime

# --- Part 1: Simulate Your Training Data (Anomaly Model) ---
data = {
    'login_attempts': [1, 2, 1, 3, 2, 1, 4, 1, 2, 5, 1, 2, 3, 1, 2, 100], # Normal users + 1 anomaly
    'failed_attempts': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 50], # Normal users + 1 anomaly
    'session_duration': [10, 12, 15, 8, 11, 14, 20, 9, 13, 25, 11, 10, 16, 12, 10, 1] # Normal users + 1 anomaly
}
df = pd.DataFrame(data)

# --- Part 2: Train the Anomaly AI Model ---
print("Training Anomaly Detection model...")
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(df)
print("Anomaly model trained.")

# --- Part 3: Create Anomaly Prediction Function ---
def get_anomaly_predictions():
    print("Generating new 'live' log data and checking for anomalies...")
    
    new_logs = []
    for _ in range(5):
        log = {
            'ip': f"192.168.1.{random.randint(10, 100)}",
            'login_attempts': random.randint(1, 5),
            'failed_attempts': random.randint(0, 2),
            'session_duration': random.randint(5, 30)
        }
        new_logs.append(log)

    anomaly_log = {
        'ip': '203.0.113.99',
        'login_attempts': 150,
        'failed_attempts': 75,
        'session_duration': 2
    }
    new_logs.append(anomaly_log)

    live_df = pd.DataFrame(new_logs)
    predictions = model.predict(live_df[['login_attempts', 'failed_attempts', 'session_duration']])
    
    alerts_list = []
    
    for index, log in enumerate(new_logs):
        if predictions[index] == -1:
            alert = {
                "timestamp": datetime.datetime.now(datetime.timezone.utc), # Added timestamp
                "threat": "Anomaly Detected (Suspicious Login Pattern)",
                "ip": log['ip'],
                "level": "High",
                "details": f"Logins: {log['login_attempts']}, Fails: {log['failed_attempts']}, Duration: {log['session_duration']}s"
            }
            alerts_list.append(alert)
            
    return alerts_list

# ===================================================================
# --- Phishing Model Section ---
# ===================================================================

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer # <-- Correct import
from sklearn.linear_model import LogisticRegression
import re

# --- Part 5: Download NLTK data ---
# This section will run to make sure the required NLTK packages are downloaded.
# NLTK is smart and will skip them if the data is already present.

print("Downloading NLTK 'punkt' tokenizer (for tokenizing words)...")
nltk.download('punkt') 

print("Downloading NLTK 'stopwords' (for filtering common words)...")
nltk.download('stopwords')

print("Downloading NLTK 'punkt_tab' (for tokenizing)...") # <-- ADD THIS
nltk.download('punkt_tab')

print("NLTK data downloads complete.")


# --- Part 6: Train Phishing Detection Model ---
print("Training Phishing Detection model...")

# 1. Create our 'dummy' training data
phishing_data = {
    'text': [
        "congratulations you won a $1000 gift card click here",
        "urgent: your account is suspended please verify your details",
        "free money just for you, click this link",
        "dear user, your password has expired. update now",
        "you have a package waiting for you, please confirm address"
    ],
    'label': [1, 1, 1, 1, 1] # 1 = Phishing
}

legit_data = {
    'text': [
        "hi team, just checking in on the project status",
        "here is the weekly report as requested",
        "meeting reminder: project sync at 10am tomorrow",
        "your order #12345 has shipped",
        "don't forget to submit your timesheet"
    ],
    'label': [0, 0, 0, 0, 0] # 0 = Legit
}

train_texts = phishing_data['text'] + legit_data['text']
train_labels = phishing_data['label'] + legit_data['label']

# 2. Create a text preprocessing function
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Preprocess all our training texts
processed_texts = [preprocess_text(text) for text in train_texts]

# 3. Create and Train the Vectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(processed_texts)

# 4. Create and Train the Classifier Model
phishing_model = LogisticRegression()
phishing_model.fit(X_train, train_labels)

print("Phishing model trained.")

# --- Part 7: Create a Phishing Prediction Function ---

def get_phishing_predictions():
    print("Generating new 'live' emails and checking for phishing...")
    
    new_emails = [
        { "sender": "security@microsft-support.com", "text": "urgent action required your account is locked click to verify" },
        { "sender": "jane.doe@company.com", "text": "here is the presentation for our 2pm meeting" },
        { "sender": "rewards@amazn-prizes.com", "text": "you have won a new laptop click here to claim your prize" }
    ]
    
    processed_new_texts = [preprocess_text(email['text']) for email in new_emails]
    X_new = vectorizer.transform(processed_new_texts)
    predictions = phishing_model.predict(X_new)
    
    alerts_list = []
    
    for index, email in enumerate(new_emails):
        if predictions[index] == 1:
            alert = {
                "timestamp": datetime.datetime.now(datetime.timezone.utc),
                "threat": "Phishing Attempt Detected",
                "source": email['sender'],
                "level": "High",
                "details": f"Email text: \"{email['text']}\""
            }
            alerts_list.append(alert)
            
    return alerts_list