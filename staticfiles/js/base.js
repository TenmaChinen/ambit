const sideBar = document.getElementById('side-bar');

sideBar.addEventListener('click', (e)=>{
  if(e.target == sideBar){
    closeNav();
  }
});

function openNav() {
  sideBar.style.display = '';
}

function closeNav() {
  sideBar.style.display = 'none';
}