const showPassword = document.querySelector('.show-password');
const passwordInput = document.getElementById('password');

showPassword.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        showPassword.textContent = 'Masquer le mot de passe';
    } else {
        passwordInput.type = 'password';
        showPassword.textContent = 'Afficher le mot de passe';
    }
});
