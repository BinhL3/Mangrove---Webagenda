function toggleNav() {
	var sidenav = document.getElementById("mySidepanel"),
    main = document.getElementById("main");
    sidenav.style.width = sidenav.style.width == "230px" ? '0' : '230px';
    main.style.marginLeft = main.style.marginLeft === "230px" ? '0' : '230px';
}

function myFunction(x) {
    x.classList.toggle("change");
}