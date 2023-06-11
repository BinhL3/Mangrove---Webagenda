function bgchange(val) {
  document.body.style.background = val;
  localStorage.setItem('backgroundColor', val);
}

// Retrieve the color from local storage on page load
window.addEventListener('load', function() {
  const savedColor = localStorage.getItem('backgroundColor');
  if (savedColor) {
    document.body.style.background = savedColor;
  }
});

