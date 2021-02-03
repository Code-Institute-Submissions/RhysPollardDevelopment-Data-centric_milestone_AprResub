$(document).ready(function () {
  // Fix found at https://api.jquery.com/toggleclass/
  // Tried ()=> but 'this' targeted window not #toggler-icon.
  // Changes the hamburger icon to an X when mobile nav opened.
  setupToggle();
});

function setupToggle() {
  $('#toggler-icon').click(function(){
    $(this).toggleClass("change");
  });
}