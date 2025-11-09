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

### 🚀 Current Status: Phase 3 Complete

1.  **Phase 1 & 2 (Backend/Frontend):** A Python **Flask** server (`app.py`) serves an **HTML/CSS/JS** dashboard. The frontend successfully fetches data from the backend API endpoint (`/api/get_alerts`).

2.  **Phase 3 (First ML Model):** The dummy API data has been replaced. We have trained a **`scikit-learn` Isolation Forest model** (`ml_models.py`) for anomaly detection. The backend API now runs this model on simulated "live" log data and sends any detected anomalies to the frontend dashboard.

---

### 💻 Tech Stack (So Far)

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **AI/ML:** Scikit-learn, Pandas
* **Environment:** venv (Virtual Environment)
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
    # Create the venv
    python -m venv venv
    
    # Activate on Windows
    .\venv\Scripts\activate
    
    # Activate on Mac/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install Flask flask-cors scikit-learn pandas
    ```

4.  **Run the backend server:**
    ```bash
    python app.py
    ```
    (You will see "Training Anomaly Detection model..." in the terminal)

5.  **View the dashboard:**
    Open your web browser and go to `http://127.0.0.1:5000/`