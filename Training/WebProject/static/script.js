const navToggle = document.getElementById("nav-toggle");
const primaryMenu = document.getElementById("primary-menu");
const dropdown = document.querySelector(".has-dropdown");

navToggle.addEventListener("click", () => {
    primaryMenu.classList.toggle("menu-open");
});

if (dropdown) {
    const trigger = dropdown.querySelector(".dropdown-trigger");

    trigger.addEventListener("click", (e) => {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            dropdown.classList.toggle("mobile-open");
        }
    });
}