$(document).ready(function () {
    bindUrlEvent();
});

function bindUrlEvent() {
    let urlInput = document.getElementById("imageUrl");
    if (urlInput)
        urlInput.addEventListener("change", loadImage);
};

function loadImage(event) {
    let url = event.currentTarget.value;
    let imgContainer = document.getElementById("imgContainer");
    imgContainer.src = url;
    let container = document.getElementsByClassName("image-container");
    container[0].classList.add("show-image");
};