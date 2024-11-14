document.addEventListener('DOMContentLoaded', () => {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
        window.history.replaceState(null, '', '/register/');  
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
        window.history.replaceState(null, '', '/login/');  
    });
});
