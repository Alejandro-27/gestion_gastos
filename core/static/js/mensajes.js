document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.auto-dismiss');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 2000); 
    });
});