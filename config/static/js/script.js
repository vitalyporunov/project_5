document.addEventListener('DOMContentLoaded', () => {
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.display = 'none';
        }, 3000);
    });
});

// Real-time form validation
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
});

// Pop-up Notifications
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'alert alert-info';
    notification.innerText = message;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
}
