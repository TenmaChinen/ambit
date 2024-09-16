
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