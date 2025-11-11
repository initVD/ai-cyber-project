# AI-Driven Cyber Threat Detection System

This project is an AI-powered system designed to detect, classify, and prevent cyber threats in real-time. It monitors system logs, emails, and user activities to identify anomalies and malicious patterns.

---

### 🎯 Project Goal

The final system will:
* Monitor system logs, emails, and user activities.
* Detect anomalies or fraud patterns using ML models.
* Trigger AI Agents that automatically respond by blocking IPs, alerting admins, or isolating users.
* Display all results on a comprehensive web dashboard.

---

### 🚀 Current Status: Phase 7 Complete (All Core Models Built)

1.  **Phase 1-2 (Backend/Frontend):** A Python **Flask** server (`app.py`) serves an **HTML/CSS/JS** dashboard.
2.  **Phase 3 (Database):** The system is connected to a **MongoDB Atlas** database to save all alerts persistently.
3.  **Phase 4 (AI/ML Engine - Module 1):** An **Isolation Forest** model (`ml_models.py`) detects log-in and behavior anomalies.
4.  **Phase 5 (AI/ML Engine - Module 2):** An **NLP-based Phishing Detector** (TF-IDF + Logistic Regression) detects malicious emails.
5.  **Phase 6 (AI/ML Engine - Module 3):** A **Random Forest Classifier** (`ml_models.py`) detects fraudulent login patterns based on user, time, device, and location.
6.  **Phase 7 (AI Agent):** An **"AI Agent" layer** (`trigger_agent_response` function) is active. It automatically adds high-threat IPs and email senders to a persistent **blocklist** in the database, which is also displayed on the dashboard.

---

### 💻 Tech Stack

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **AI/ML:** Scikit-learn, Pandas, NLTK
* **Database:** MongoDB (via `pymongo` and