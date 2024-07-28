const modal = document.getElementById('modal');
const btnPositive = modal.querySelector('#btn-positive');
const btnNegative = modal.querySelector('#btn-negative');

btnPositive.addEventListener('click', (e)=>{
  handleModalAction(btnPositive);
});

btnNegative.addEventListener('click', (e)=>{
  handleModalAction(btnNegative);
});

modal.addEventListener('click', (e)=>{
  if (e.target == modal){
    hideModal();
  }
})

function showModal(){
  modal.style.display = '';
}

function hideModal(){
  modal.style.display = 'none';
}

