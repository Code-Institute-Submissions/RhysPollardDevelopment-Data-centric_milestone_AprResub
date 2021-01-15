$(document).ready(function () {

})
  
  // Finds results id when search is posted and scrolls to results on page.
  // https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
  var results = document.getElementById("results")
  if (results)
    results.scrollIntoView({ behavior: "smooth" });
  