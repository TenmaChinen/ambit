const formFilter = document.getElementById('form-filter');
const modalFilter = document.getElementById('modal-filter');
const btnModalClose = document.getElementById('btn-modal-close');
const btnShowMore = document.getElementById('btn-show-more');
const divAdvancedForm = document.getElementById('div-advanced-form');

function toggleModalFilter(){
  const state = modalFilter.style.display === 'none';
  modalFilter.style.display = state ? '' : 'none';
}

function toggleAdvancedForm(){
  const state = divAdvancedForm.style.display === 'none';
  divAdvancedForm.style.display = state ? '' : 'none';
  btnShowMore.innerHTML = state ? 'Mostrar menos' : 'Mostrar más';
}


btnModalClose.addEventListener('click', (e)=>{
  modalFilter.style.display = 'none';
});



formFilter.addEventListener('submit', (event)=> {
    event.preventDefault(); // Prevent the default form submission

    // const form = event.target;
    const params = new URLSearchParams();

    const formData = new FormData(formFilter);
    formData.forEach((value,name) => {
        if (value){
            params.append(name,value);
        }
    });

    // Construct the URL
    const url = `${formFilter.action}?${params.toString()}`;

    // Redirect to the constructed URL
    window.location.href = url;
});