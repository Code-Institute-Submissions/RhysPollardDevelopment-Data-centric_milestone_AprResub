let password = document.getElementById("password");
let confirm_password = document.getElementById("confirm_password");

// Keyup code refined using mozilla site
// https://developer.mozilla.org/en-US/docs/Web/API/Document/keyup_event
if (password) {
    password.addEventListener('keyup', validatePassword);
    confirm_password.addEventListener('keyup', validatePassword);
}

// Checks that both Passwords are same after each character and sets the
// warning for validity.
// Idea for validate password found at https://codepen.io/diegoleme/pen/surIK
// https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/setCustomValidity
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