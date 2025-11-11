// --- NEW: Run this code first! ---
const token = localStorage.getItem("access_token");
if (!token) {
    // No token found, redirect to login page
    window.location.href = "/login";
}

// --- NEW: Create auth headers to send with requests ---
const authHeaders = {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
};

// This function runs when the page is loaded
document.addEventListener("DOMContentLoaded", () => {
    
    // Load dashboard data
    fetchAlerts();
    fetchBlocklist();

    // --- NEW: Logout Button Logic ---
    const logoutButton = document.getElementById("logout-btn");
    logoutButton.addEventListener("click", () => {
        // Clear the token
        localStorage.removeItem("access_token");
        // Send user back to login
        window.location.href = "/login";
    });
});

// --- UPDATED: Function to load alerts ---
function fetchAlerts() {
    const alertsContainer = document.getElementById("alerts-container");
    const API_URL = "http://127.0.0.1:5000/api/get_alerts";

    fetch(API_URL, {
        method: "GET",
        headers: authHeaders // <-- NEW: Send authorization header
    })
    .then(response => {
        if (response.status === 401) { // Unauthorized (bad token)
            localStorage.removeItem("access_token");
            window.location.href = "/login";
        }
        return response.json();
    })
    .then(alerts => {
        alertsContainer.innerHTML = "";
        if (!alerts || alerts.length === 0) {
            alertsContainer.innerHTML = "<p>No alerts to show.</p>";
            return;
        }

        alerts.forEach(alert => {
            const alertElement = document.createElement("div");
            alertElement.classList.add("alert-card");
            
            if (alert.level === 'High') alertElement.classList.add("level-high");
            else if (alert.level === 'Medium') alertElement.classList.add("level-medium");
            else alertElement.classList.add("level-low");

            let sourceField = '';
            if (alert.ip) sourceField = `<p><strong>IP Address:</strong> ${alert.ip}</p>`;
            else if (alert.source) sourceField = `<p><strong>Source:</strong> ${alert.source}</p>`;

            const timestamp = new Date(alert.timestamp.$date).toLocaleString();

            alertElement.innerHTML = `
                <h3>${alert.threat}</h3>
                ${sourceField}
                <p><strong>Risk Level:</strong> ${alert.level}</p>
                ${alert.details ? `<p class="details"><strong>Details:</strong> ${alert.details}</p>` : ''}
                <p class="timestamp">${timestamp}</p>
            `;
            alertsContainer.appendChild(alertElement);
        });
    })
    .catch(error => {
        console.error("Error fetching alerts:", error);
        alertsContainer.innerHTML = "<p>Error loading alerts.</p>";
    });
}

// --- UPDATED: Function to load the blocklist ---
function fetchBlocklist() {
    const blocklistBody = document.getElementById("blocklist-body");
    const API_URL = "http://127.0.0.1:5000/api/get_blocklist";

    fetch(API_URL, {
        method: "GET",
        headers: authHeaders // <-- NEW: Send authorization header
    })
    .then(response => {
        if (response.status === 401) { // Unauthorized
            localStorage.removeItem("access_token");
            window.location.href = "/login";
        }
        return response.json();
    })
    .then(blocklistItems => {
        blocklistBody.innerHTML = "";
        if (!blocklistItems || blocklistItems.length === 0) {
            blocklistBody.innerHTML = '<tr><td colspan="4">Blocklist is empty.</td></tr>';
            return;
        }

        blocklistItems.forEach(item => {
            const timestamp = new Date(item.blocked_on.$date).toLocaleString();
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.identifier}</td>
                <td>${item.type}</td>
                <td>${item.reason}</td>
                <td>${timestamp}</td>
            `;
            blocklistBody.appendChild(row);
        });
    })
    .catch(error => {
        console.error("Error fetching blocklist:", error);
        blocklistBody.innerHTML = '<tr><td colspan="4">Error loading blocklist.</td></tr>';
    });
}