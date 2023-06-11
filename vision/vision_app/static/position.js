var container = document.getElementById("my-container");
var containerOffset = container.offsetTop;

window.addEventListener("load", function() {
  container.style.position = "absolute";
  container.style.top = containerOffset + "px";
});

function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}