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

function showSuggestions() {
    let query = document.getElementById("searchInput").value;

    if (query.length < 1) {
        document.getElementById("suggestionBox").innerHTML = "";
        return;
    }

    fetch(`/suggest?q=${query}`)
        .then(response => response.json())
        .then(data => {
            let suggestionBox = document.getElementById("suggestionBox");
            suggestionBox.innerHTML = "";

            data.forEach(item => {
                let div = document.createElement("div");
                div.innerText = item;
                div.onclick = function () {
                    document.getElementById("searchInput").value = item;
                    suggestionBox.innerHTML = "";
                };
                suggestionBox.appendChild(div);
            });
        });
}