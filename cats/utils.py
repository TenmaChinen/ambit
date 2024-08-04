from io import BytesIO
from PIL import Image

def to_thumbnail(image_file):
    im_pil = Image.open(image_file)
    im_pil = im_pil.resize(size=(100,100), resample= Image.BILINEAR)
    bytes_io = BytesIO()
    im_pil.save(bytes_io, format='JPEG')
    return bytes_io


def format_image_name(cat_id):
    return f'{cat_id:010}.jpg'


