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

### 🚀 Current Status: Phase 1 & 2 Complete

At this stage, the project's foundational structure is complete. We have a working full-stack application that includes:

1.  **Backend Server:** A Python **Flask** server (`app.py`) that serves the frontend application and provides a basic API endpoint (`/api/get_alerts`).
2.  **Frontend Dashboard:** A web dashboard built with **HTML** (`index.html`), **CSS** (`style.css`), and **JavaScript** (`app.js`).
3.  **API Connection:** The JavaScript on the frontend successfully fetches (dummy) threat data from the Flask backend API and displays it dynamically on the page.

---

### 💻 Tech Stack (So Far)

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
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
    pip install Flask flask-cors
    ```

4.  **Run the backend server:**
    ```bash
    python app.py
    ```

5.  **View the dashboard:**
    Open your web browser and go to `http://127.0.0.1:5000/`