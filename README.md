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

### 🚀 Current Status: Phase 8 Complete (Fully Secured)

1.  **Phase 1-2 (Backend/Frontend):** A Python **Flask** server (`app.py`) serves an **HTML/CSS/JS** dashboard.
2.  **Phase 3 (Database):** The system is connected to a **MongoDB Atlas** database to save all alerts persistently.
3.  **Phase 4 (AI/ML Engine - Module 1):** An **Isolation Forest** model (`ml_models.py`) detects log-in and behavior anomalies.
4.  **Phase 5 (AI/ML Engine - Module 2):** An **NLP-based Phishing Detector** (TF-IDF + Logistic Regression) detects malicious emails.
5.  **Phase 6 (AI/ML Engine - Module 3):** A **Random Forest Classifier** (`ml_models.py`) detects fraudulent login patterns.
6.  **Phase 7 (AI Agent):** An **"AI Agent" layer** automatically adds high-threat IPs and email senders to a persistent **blocklist**.
7.  **Phase 8 (Security):** The application is now secured with **JWT (JSON Web Token) authentication**. All dashboard and API routes are protected, and users are required to log in via a new, secure login page.

---

### 💻 Tech Stack

* **Backend:** Python, Flask, Flask-JWT-Extended, Flask-CORS
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
    pip install Flask flask-cors scikit-learn pandas pymongo nltk Flask-JWT-Extended
    ```

4.  **Create your configuration file:**
    * In the root folder, create a file named `config.py`.
    * Add your MongoDB URI and a JWT secret key:
      ```python
      MONGO_URI = "YOUR_MONGODB_CONNECTION_STRING"
      JWT_SECRET_KEY = "YOUR_OWN_SUPER_SECRET_KEY"
      ```
    * (This file is in `.gitignore` and will not be pushed to GitHub).

5.  **Run the backend server:**
    ```bash
    python app.py
    ```

6.  **View the dashboard:**
    Open your web browser and go to `http://127.0.0.1:5000/`. You will be redirected to the login page.
    * **Demo Username:** `admin`
    * **Demo Password:** `password123`