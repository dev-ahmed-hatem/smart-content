const pageTop = document.getElementById("top"),
    scrollTop = document.getElementById("scroll"),
    categoriesToggler = document.getElementById("categories-toggler"),
    categories = document.getElementById("categories");

scrollTop.addEventListener("click", function () {
    pageTop.scrollIntoView();
});

function checkScrollTop() {
    if (document.documentElement.scrollTop > 200) {
        scrollTop.classList.add("active");
    } else {
        scrollTop.classList.remove("active");
    }
}

/*categoriesToggler.addEventListener("click", function () {
    categories.classList.toggle("active");
});*/

window.addEventListener("scroll", checkScrollTop);
