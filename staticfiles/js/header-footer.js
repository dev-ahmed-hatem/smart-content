const header = document.getElementById("header"),
    toggle = document.getElementById("toggle"),
    links = document.getElementById("links");

function headerStick() {
    if (document.documentElement.scrollTop > header.clientHeight) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

toggle.addEventListener("click", function () {
    this.classList.toggle("active");
    links.classList.toggle("active");
});

window.addEventListener("scroll", () => {
    headerStick();
});
