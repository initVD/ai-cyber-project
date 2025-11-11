// This function runs when the webpage is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    
    // Run both functions to load all data
    fetchAlerts();
    fetchBlocklist();

});

// --- NEW: Function to load alerts ---
function fetchAlerts() {
    const alertsContainer = document.getElementById("alerts-container");
    const API_URL = "http://127.0.0.1:5000/api/get_alerts";

    fetch(API_URL)
        .then(response => response.json())
        .then(alerts => {
            alertsContainer.innerHTML = ""; // Clear 'Loading...'

            if (!alerts || alerts.length === 0) {
                alertsContainer.innerHTML = "<p>No alerts to show.</p>";
                return;
            }

            alerts.forEach(alert => {
                const alertElement = document.createElement("div");
                alertElement.classList.add("alert-card");
                
                if (alert.level === 'High') {
                    alertElement.classList.add("level-high");
                } else if (alert.level === 'Medium') {
                    alertElement.classList.add("level-medium");
                } else {
                    alertElement.classList.add("level-low");
                }

                // Smartly show IP or Source
                let sourceField = '';
                if (alert.ip) {
                    sourceField = `<p><strong>IP Address:</strong> ${alert.ip}</p>`;
                } else if (alert.source) {
                    sourceField = `<p><strong>Source:</strong> ${alert.source}</p>`;
                }

                // Use .toLocaleString() for readable timestamps
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
            alertsContainer.innerHTML = "<p>Error loading alerts. Is the server running?</p>";
        });
}

// --- NEW: Function to load the blocklist ---
function fetchBlocklist() {
    const blocklistBody = document.getElementById("blocklist-body");
    const API_URL = "http://127.0.0.1:5000/api/get_blocklist";

    fetch(API_URL)
        .then(response => response.json())
        .then(blocklistItems => {
            blocklistBody.innerHTML = ""; // Clear 'Loading...'

            if (!blocklistItems || blocklistItems.length === 0) {
                blocklistBody.innerHTML = '<tr><td colspan="4">Blocklist is empty.</td></tr>';
                return;
            }

            blocklistItems.forEach(item => {
                const timestamp = new Date(item.blocked_on.$date).toLocaleString();
                
                // Create a new table row
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