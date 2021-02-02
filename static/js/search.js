$(document).ready(function () {
  scrollResults();
  newPage();
})
  
// Finds results id when search is posted and scrolls to results on page.
// https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
function scrollResults(){
  var results = document.getElementById("results")
  if (results)
    results.scrollIntoView({ behavior: "smooth" });
}

function newPage(){
  var paginateResults = document.getElementById("paginate")
  if (paginateResults)
    paginateResults.scrollIntoView();
}
  