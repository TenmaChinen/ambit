const modalCensus = document.getElementById('modal-census');
modalCensus.querySelector('#btn-modal-close').addEventListener('click', (e)=>{
  modalCensus.style.display = 'none';
});

modalCensus.addEventListener('click', (e)=>{
  if( e.target== modalCensus){
    modalCensus.style.display = 'none';
  }
})

// Option Menu

function handleOptionMenuClick(listItem){
  switch(listItem.id){
  case 'option-create-census':
    const state = modalCensus.style.display === 'none';
    modalCensus.style.display = state ? '' : 'none';
    break;
  }
}

// Modal

// function handleModalAction(btnOption){
//   if (btnOption.id === 'btn-positive'){
//     window.location.href = btnOption.getAttribute('data');
//   }else if (btnOption.id === 'btn-negative'){
//     hideModal();
//   }
// }