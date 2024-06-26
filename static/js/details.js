
// JavaScript to handle toggling of navigation links on mobile
document.addEventListener("DOMContentLoaded", function () {
    const navbarToggle = document.querySelector(".navbar-toggler");
    const navbarNav = document.querySelector("#navbarNav");

    navbarToggle.addEventListener("click", function () {
        if (navbarNav.classList.contains("show")) {
            // If the navigation is already shown, hide it
            navbarNav.classList.remove("show");
        } else {
            // If the navigation is hidden, show it
            navbarNav.classList.add("show");
        }
    });
});


/*scroll navbar*/
window.addEventListener("scroll", function () {
    var nav = document.querySelector("#mainNav");
    if (window.scrollY > 50) {
        nav.classList.add("navbar-scrolled");
    } else {
        nav.classList.remove("navbar-scrolled");
    }
});


/*navbar dropdown hover*/
function showDropdown(element) {
    var dropdownMenu = element.querySelector('.dropdown-menu');
    dropdownMenu.classList.add('show');
}

function hideDropdown(element) {
    var dropdownMenu = element.querySelector('.dropdown-menu');
    dropdownMenu.classList.remove('show');
}


/**** Arrow ****/
window.onload = function () {
    var arrow = document.getElementById('arrow');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 20) {
            arrow.style.display = "block";
        } else {
            arrow.style.display = "none";
        }
    });

    // Smooth scroll to top when arrow is clicked
    arrow.onclick = function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };
};
