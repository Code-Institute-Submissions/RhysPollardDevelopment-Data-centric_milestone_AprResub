$(document).ready(function () {
  // Fix found at https://api.jquery.com/toggleclass/
  // Tried ()=> but 'this' targeted window now #toggler-icon.
  // Changes the hamburger icon to an X when mobile nav opened.
  $('#toggler-icon').click(function(){
    $(this).toggleClass("change")
  })
  
  // Finds results id when search is posted and scrolls to results on page.
  // https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
  var results = document.getElementById("results")
  if(results)
    results.scrollIntoView({ behavior: "smooth" });
});

let password = document.getElementById("password");
let confirm_password = document.getElementById("confirm_password");

// Keyup code refined using mozilla site
// https://developer.mozilla.org/en-US/docs/Web/API/Document/keyup_event
if (password) {
    password.addEventListener('keyup', validatePassword);
    confirm_password.addEventListener('keyup', validatePassword);
}

/* Checks that both Passwords are same after each character and sets the
warning for validity.
Idea for validate password found at https://codepen.io/diegoleme/pen/surIK
*/ https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/setCustomValidity
function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords do not match!");
    }
    else {
        confirm_password.setCustomValidity("");
    }
}

// Code from bootstrap for their validation styles.
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

/*
Confirm that the user wants to delete a recipe and delete it if so.
Args:
  recipe_delete_url: string. The URL endpoint to delete a given recipe.
*/

function confirm_delete(recipe_delete_url){
  var delete_confirmed = confirm("Delete this recipe?")
  if (delete_confirmed){
      window.location.href = recipe_delete_url;
  }
}


/* Checks the state of a pages heart icon and updates user data
 with route name as required. Advice found at:
 https://stackoverflow.com/questions/37631388/how-to-get-data-in-flask-from-ajax-post*/
let fav_icon = document.getElementById("favourite")
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
