const btnOptionMenu = document.getElementById('btn-option-menu');
const divOptionMenu = document.getElementById('option-menu');

btnOptionMenu.addEventListener('click', (e)=>{
  const state = divOptionMenu.style.display === 'none';
  divOptionMenu.style.display = state ? '' : 'none';
  divOptionMenu.focus();
});

divOptionMenu.addEventListener('click', (e)=>{
  divOptionMenu.style.display = 'none';
});

const optionMenuItems = divOptionMenu.querySelectorAll('ul li');

for (const listItem of optionMenuItems) {
    listItem.addEventListener('click', (e)=>{
        handleOptionMenuClick(listItem);
    });
}
