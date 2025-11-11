document.addEventListener("DOMContentLoaded", () => {
    
    const alertsContainer = document.getElementById("alerts-container");
    const API_URL = "http://127.0.0.1:5000/api/get_alerts";

    fetch(API_URL)
        .then(response => response.json())
        .then(alerts => {
            alertsContainer.innerHTML = ""; // Clear 'Loading...'

            if (alerts.length === 0) {
                alertsContainer.innerHTML = "<p>No alerts to show.</p>";
                return;
            }

            alerts.forEach(alert => {
                const alertElement = document.createElement("div");
                alertElement.classList.add("alert-card");
                
                // Add a CSS class based on the alert level
                if (alert.level === 'High') {
                    alertElement.classList.add("level-high");
                } else if (alert.level === 'Medium') {
                    alertElement.classList.add("level-medium");
                } else {
                    alertElement.classList.add("level-low");
                }

                //// Format the timestamp to be more readable
                const timestamp = new Date(alert.timestamp).toLocaleString();

                // --- UPDATED HTML to show the new 'details' field ---
                // Check if the alert has an IP or a Source
                let sourceField = '';
                if (alert.ip) {
                    sourceField = `<p><strong>IP Address:</strong> ${alert.ip}</p>`;
                } else if (alert.source) {
                    sourceField = `<p><strong>Source:</strong> ${alert.source}</p>`;
                }

                alertElement.innerHTML = `
                    <h3>${alert.threat}</h3>
                    ${sourceField} <p><strong>Risk Level:</strong> ${alert.level}</p>
                    ${alert.details ? `<p class="details"><strong>Details:</strong> ${alert.details}</p>` : ''}
                    <p class="timestamp">${timestamp}</p>
                `;
                // The ${... ? ... : ''} part means: "Only add this line if 'alert.details' exists"
                
                alertsContainer.appendChild(alertElement);
            });
        })
        .catch(error => {
            console.error("Error fetching alerts:", error);
            alertsContainer.innerHTML = "<p>Error loading alerts. Is the server running?</p>";
        });
});