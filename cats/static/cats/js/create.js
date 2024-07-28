const checkboxSterilized = document.getElementById('id_sterilized');
const inputSterilizeDate = document.getElementById('id_sterlize_date');

const divHiddenPanel = document.getElementById('hidden-panel');
const btnShowMore = document.getElementById('btn-show-more');

function updateSterilizeDateVisibility(){
    inputSterilizeDate.disabled= (!checkboxSterilized.checked);
}

updateSterilizeDateVisibility();

checkboxSterilized.addEventListener('change', (e)=>{
  updateSterilizeDateVisibility();
});

btnShowMore.addEventListener('click', (e)=>{
  const state = divHiddenPanel.style.display ==='none';
  divHiddenPanel.style.display = state ? '' : 'none';
  btnShowMore.innerHTML = state ? 'Mostrar menos' : 'Mostrar más';
});

// Image Placeholder
const btnImagePlaceholder = document.getElementById('btn-image-placeholder');
const inputPhoto = document.getElementById('id_photo');
const imageTray = document.getElementById('image-tray');
const icImagePlaceholder = document.getElementById('ic-image-placeholder');
const divCropContainer = document.getElementById('div-crop-container');

btnImagePlaceholder.addEventListener('click', (e) => {
  inputPhoto.click();
});

inputPhoto.addEventListener('change', (e)=>{
  const file = inputPhoto.files[0];
  if (!file) return;
  const fileReader = new FileReader();
  fileReader.onload = function(e) {
      const img = new Image();
      img.src = e.target.result;
      img.onload = function() {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0);

          canvas.toBlob( function(blob) {
            loadImageToCrop(blob);
          }, 'image/jpeg', 1);
      }
  }
  fileReader.readAsDataURL(file);
  event.target.value = '';
});


function displayCroppedImage(blob){
    imageTray.style.display='';
    icImagePlaceholder.style.display='none';
    
    imageTray.src = URL.createObjectURL(blob);

    const newFile = new File([blob], 'image.jpg', {type: 'image/jpeg'});
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(newFile);
    inputPhoto.files = dataTransfer.files;
}