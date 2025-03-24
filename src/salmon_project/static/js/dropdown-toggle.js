// Script for handling the Edit and Delete post 
// for vertical three dots menu in the user's profile.

document.addEventListener("DOMContentLoaded", function() {
    // Select all dropdown toggle buttons
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(event) {
            event.stopPropagation(); // This prevents the click from bubbling up
            const dropdownMenu = this.nextElementSibling;
            if (dropdownMenu) {
                dropdownMenu.classList.toggle('show');
            }
        });
    });

    document.addEventListener('click', function() {
        document.querySelectorAll('.dropdown-menu.show').forEach(function(menu) {
            menu.classList.remove('show');
        });
    });
});
