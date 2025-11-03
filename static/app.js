// This function runs when the webpage is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    
    // Find the <div> on our HTML page with the ID "alerts-container"
    const alertsContainer = document.getElementById("alerts-container");

    // This is the URL of the API you built in Flask
    const API_URL = "http://127.0.0.1:5000/api/get_alerts";

    // Use the 'fetch' function to get data from your API
    fetch(API_URL)
        .then(response => response.json()) // Convert the response to JSON
        .then(alerts => {
            // 'alerts' is now our list of dummy data from Python
            
            // Clear the "Loading alerts..." text
            alertsContainer.innerHTML = "";

            if (alerts.length === 0) {
                alertsContainer.innerHTML = "<p>No alerts to show.</p>";
                return;
            }

            // Loop through each alert in the list
            alerts.forEach(alert => {
                // Create a new <div> for this alert
                const alertElement = document.createElement("div");
                
                // Add a CSS class (for styling later)
                alertElement.classList.add("alert-card");
                
                // Add the alert data as HTML
                alertElement.innerHTML = `
                    <h3>${alert.threat}</h3>
                    <p><strong>IP Address:</strong> ${alert.ip}</p>
                    <p><strong>Risk Level:</strong> ${alert.level}</p>
                `;
                
                // Add the new <div> to our main container
                alertsContainer.appendChild(alertElement);
            });
        })
        .catch(error => {
            // If something goes wrong (e.g., server is off)
            console.error("Error fetching alerts:", error);
            alertsContainer.innerHTML = "<p>Error loading alerts. Is the server running?</p>";
        });
});