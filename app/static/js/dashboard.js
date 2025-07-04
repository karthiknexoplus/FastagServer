document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarUnfoldBtn = document.getElementById('sidebarUnfoldBtn');
    const darkModeToggle = document.getElementById('darkModeToggle');
    const searchInput = document.getElementById('sidebarSearch');
    const menuItems = document.querySelectorAll('.menu-item.has-submenu');

    // Sidebar expand using unfold logo button
    if (sidebarUnfoldBtn) {
        sidebarUnfoldBtn.addEventListener('click', function() {
            sidebar.classList.remove('collapsed');
        });
        sidebarUnfoldBtn.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                sidebar.classList.remove('collapsed');
            }
        });
    }

    // Sidebar collapse using logo in expanded header
    const sidebarHeaderLogo = document.querySelector('.sidebar-header-expanded .sidebar-logo');
    if (sidebarHeaderLogo) {
        sidebarHeaderLogo.style.cursor = 'pointer';
        sidebarHeaderLogo.addEventListener('click', function() {
            sidebar.classList.add('collapsed');
        });
    }

    // Submenu toggle
    menuItems.forEach(item => {
        item.querySelector('.submenu-toggle').addEventListener('click', function(e) {
            e.preventDefault();
            item.classList.toggle('open');
        });
    });

    // Sidebar search filter
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        document.querySelectorAll('.sidebar-menu > .menu-item').forEach(item => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
        });
    });

    // Dark mode toggle
    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        sidebar.classList.toggle('dark-mode');
        document.querySelector('.dashboard-content').classList.toggle('dark-mode');
        document.querySelector('.dashboard-header').classList.toggle('dark-mode');
        document.querySelector('.dashboard-notifications').classList.toggle('dark-mode');
    });

    // Responsive: close sidebar on outside click (mobile)
    document.addEventListener('click', function(e) {
        if(window.innerWidth < 900 && sidebar.classList.contains('open')) {
            if(!sidebar.contains(e.target) && !sidebarUnfoldBtn.contains(e.target)) {
                sidebar.classList.remove('open');
            }
        }
    });
}); 