// Toggle between sign-in and sign-up forms
const loginButton = document.getElementById("login");
const registerButton = document.getElementById("register");
const container = document.getElementById("container");

registerButton.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

loginButton.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

// Add simple validation for empty fields (can be enhanced as needed)
document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", function(event) {
        const email = this.querySelector("input[type='email']");
        const password = this.querySelector("input[type='password']");
        if (!email.value || !password.value) {
            alert("Please fill in both email and password.");
            event.preventDefault();
        }
    });
});
