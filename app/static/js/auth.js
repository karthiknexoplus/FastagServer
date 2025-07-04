// Animate form and image on page load
window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.animate-form').forEach(el => {
        el.classList.add('show');
    });
    document.querySelectorAll('.animate-img').forEach(el => {
        el.classList.add('show');
    });
}); 