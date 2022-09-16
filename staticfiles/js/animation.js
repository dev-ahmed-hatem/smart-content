const targets = document.querySelectorAll(".animated");

function checkTargets() {
    targets.forEach((el, key) => {
        if (
            document.documentElement.clientHeight -
                el.getBoundingClientRect().y >=
                100 &&
            el.getBoundingClientRect().height + el.getBoundingClientRect().y >=
                130
        ) {
            el.classList.add("visible");
        } else {
            el.classList.remove("visible");
        }
    });
}

window.addEventListener("scroll", () => {
    checkTargets();
});
