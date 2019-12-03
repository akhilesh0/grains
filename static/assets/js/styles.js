function myFunction(x) {
  x.classList.toggle("fa-chevron-right");
  var e = document.getElementById("mySidenav");
    if (e.style.width == '0px')
    {
        e.style.width = '260px';
    }
    else 
    {
        e.style.width = '0px';
    }
}