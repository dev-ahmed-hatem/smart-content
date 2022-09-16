const searchBtn = document.getElementById("search-btn"),
    searchText = document.getElementById("search-text");

searchBtn.addEventListener("click", function () {
    searchBtn.classList.add("active");
    searchText.focus();
});

searchText.addEventListener("focusout", function () {
    searchBtn.classList.remove("active");
});
