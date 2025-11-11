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

### 🚀 Current Status: Phase 5 Complete

1.  **Phase 1-2 (Backend/Frontend):** A Python **Flask** server (`app.py`) serves an **HTML/CSS/JS** dashboard.
2.  **Phase 3 (Model 1):** An **Isolation Forest** model (`ml_models.py`) is trained to detect log-in and behavior anomalies.
3.  **Phase 4 (Database):** The system is connected to a **MongoDB Atlas** database. All detected alerts are automatically saved persistently.
4.  **Phase 5 (Model 2):** A second **NLP-based Phishing Detector** (TF-IDF + Logistic Regression) has been added. The system now detects both anomalous behavior and phishing emails.

---

### 💻 Tech Stack (So Far)

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **AI/ML:** Scikit-learn, Pandas, NLTK
* **Database:** MongoDB (via `pymongo` and MongoDB Atlas)
* **Environment:** venv
* **Version Control:** Git & GitHub

---

### 🛠️ How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install Flask flask-cors scikit-learn pandas pymongo nltk
    ```

4.  **Create your configuration file:**
    * In the root folder, create a file named `config.py`.
    * Add one line: `MONGO_URI = "YOUR_MONGODB_CONNECTION_STRING"`
    * (This file is in `.gitignore` and will not be pushed to GitHub).

5.  **Run the backend server:**
    ```bash
    python app.py
    ```

6.  **View the dashboard:**
    Open your web browser and go to `http://127.0.0.1:5000/`