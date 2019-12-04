document.querySelector('#side-collapse').addEventListener('click', collapse);
    
function collapse() {
  this.classList.toggle('fa-chevron-right');
  this.classList.toggle('fa-chevron-left');
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
