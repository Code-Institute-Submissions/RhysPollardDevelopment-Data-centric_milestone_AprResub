$(document).ready(function () {
    bindFavourite();
});

/* Checks the state of a pages heart icon and updates user data
 with route name as required. Advice found at:
 https://stackoverflow.com/questions/37631388/how-to-get-data-in-flask-from-ajax-post*/

function bindFavourite() {
  let fav_icon = document.getElementById("favourite")
  if (fav_icon) {
    fav_icon.addEventListener("change", function () {
    url = window.location.pathname
    url = url.replace("/show_route/", "")
    /* need full version of ajax apparently */
    $.ajax({
      type:"POST",
      url: '/toggle_favourite',
      data: {
        id: url,
        checkbox: fav_icon.checked
        }
      })
    })
  }
}

