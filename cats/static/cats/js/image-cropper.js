const imageCrop = document.getElementById('image-crop');
const btnCropClose = document.getElementById('btn-crop-close');
const btnCropSave = document.getElementById('btn-crop-save');

let cropper;

imageCrop.addEventListener('load', function(event){
  divCropContainer.style.display = '';
  if (cropper) {
    cropper.destroy();
  }
   cropper = new Cropper(imageCrop, {
    autoCrop:false,
    aspectRatio: 1,
    viewMode:2, // 0 : No Restrictions | 1 : cropbox not exceed canvas | 2 : Canvas fit container
    guides:false,
    center:false,
    ready : function() {
      cropper.crop();
    }
  });
});


btnCropClose.addEventListener('click', (e)=> {
  finishCropMenu();
});

btnCropSave.addEventListener('click', (e)=> {
  saveCroppedImage();
  finishCropMenu();
});

function finishCropMenu(){
  divCropContainer.style.display = 'none';
  cropper.destroy();
}

function loadImageToCrop(blob){
  const url = URL.createObjectURL(blob);
  imageCrop.src = url;
}

function saveCroppedImage(){
  const croppedCanvas = cropper.getCroppedCanvas({
    maxHeight:600, //400
    imageSmoothingEnabled:true,
    imageSmoothingQuality:'high'
  }); 

  const croppedImage = croppedCanvas.toBlob((blob) =>{
    displayCroppedImage(blob);
  }, 'image/jpeg',1);
}