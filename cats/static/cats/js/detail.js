const divDetailTable = document.getElementById('div-detail-table');
const btnShowMore = document.getElementById('btn-show-more');

btnShowMore.addEventListener('click', (e)=>{
  const state = divDetailTable.style.display === 'none';
  divDetailTable.style.display = state ? '' : 'none';
  btnShowMore.innerHTML = state ? 'Mostrar menos' : 'Mostrar más';
});

// Option Menu

function handleOptionMenuClick(listItem){
  switch(listItem.id){
  case 'option-edit':
    window.location.href = listItem.getAttribute('data');
    break;
  case 'option-delete':
    showModal();
    break;  
  }
}

// Modal

function handleModalAction(btnOption){
  if (btnOption.id === 'btn-positive'){
    window.location.href = btnOption.getAttribute('data');
  }else if (btnOption.id === 'btn-negative'){
    hideModal();
  }
}