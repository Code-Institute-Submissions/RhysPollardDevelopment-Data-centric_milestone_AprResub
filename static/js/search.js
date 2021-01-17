$(document).ready(function () {
  scrollResults();
})
  
// Finds results id when search is posted and scrolls to results on page.
// https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
function scrollResults(){
  var results = document.getElementById("results")
  if (results)
    results.scrollIntoView({ behavior: "smooth" });
}
  