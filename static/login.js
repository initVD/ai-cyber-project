document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");
    const errorMessage = document.getElementById("error-message");

    loginForm.addEventListener("submit", (e) => {
        // Prevent the form from submitting normally
        e.preventDefault();

        const username = loginForm.username.value;
        const password = loginForm.password.value;

        // Send the login data to our new /api/login endpoint
        fetch("http://127.0.0.1:5000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.access_token) {
                // SUCCESS! Save the token
                localStorage.setItem("access_token", data.access_token);
                // Redirect to the (now protected) dashboard
                window.location.href = "/";
            } else {
                // Failed login
                errorMessage.textContent = data.msg || "Invalid username or password.";
            }
        })
        .catch(error => {
            console.error("Login error:", error);
            errorMessage.textContent = "An error occurred. Please try again.";
        });
    });
});