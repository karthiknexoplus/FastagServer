document.addEventListener('DOMContentLoaded', function() {
    // Topnav submenu toggle
    document.querySelectorAll('.menu-item.has-submenu .submenu-toggle').forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const parent = this.closest('.menu-item');
            parent.classList.toggle('open');
        });
    });
}); 