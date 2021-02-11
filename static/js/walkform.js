$(document).ready(function () {
    bindUrlEvent();
});

function bindUrlEvent() {
    let urlInput = document.getElementById("imageUrl");
    if (urlInput)
        urlInput.addEventListener("change", loadImage);
};

/* idea for url validator found at 
https://stackoverflow.com/questions/31398473/
load-image-in-div-from-url-obtained-from-a-text-box */
function loadImage(event) {
    let url = event.currentTarget.value;
    let imgContainer = document.getElementById("imgContainer");
    imgContainer.src = url;
    let container = document.getElementsByClassName("image-container");
    container[0].classList.add("show-image");
};