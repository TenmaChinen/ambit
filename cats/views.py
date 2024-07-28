from django.shortcuts import render, redirect
from cats.forms import FormCat, FormCatFilter
from colonies.models import Colony
from cats.models import Cat
from io import BytesIO
from PIL import Image
import pdb


def to_thumbnail(image_file):
    im_pil = Image.open(image_file)
    im_pil = im_pil.resize(size=(100,100), resample= Image.BILINEAR)
    bytes_io = BytesIO()
    im_pil.save(bytes_io, format='JPEG')
    return bytes_io


def create_view(request):

    if request.method == 'POST':
        form_cat = FormCat(data=request.POST, files=request.FILES)
        if form_cat.is_valid():
            cat = form_cat.save(commit=True)
            bytes_io = to_thumbnail(cat.photo)
            cat.thumbnail.save(name=f'image-{cat.id}.jpg', content=bytes_io, save=True)
            
            # Add QueryDict META here?
            return redirect('cats:list')
    else:
        form_cat = FormCat(initial=request.GET.dict())

    context = dict(form_cat = form_cat)
    return render(request, 'cats/create.html', context)


def list_view(request):
    d_querydict = request.GET.dict()
    form_cat_filter = FormCatFilter(data=d_querydict)
    
    d_querydict = {k: v for k, v in d_querydict.items() if v}
    
    if 'name' in d_querydict:
        d_querydict['name__contains'] = d_querydict.pop('name')

    records = Cat.objects.filter(**d_querydict)
    records = records.order_by('name', 'frequency')
    
    context = dict(list_cat=records, form_cat_filter=form_cat_filter)

    if 'colony' in d_querydict:
        context['colony'] = Colony.objects.get(id=d_querydict['colony'])

    return render(request, 'cats/list.html', context)


def detail_view(request,pk):
    cat = Cat.objects.get(id=pk)
    context = dict(cat=cat)
    return render(request, 'cats/detail.html', context)


def update_view(request,pk):
    cat = Cat.objects.get(id=pk)

    if request.method == 'POST':
        form_cat = FormCat(data=request.POST, files=request.FILES, instance=cat)
        if form_cat.is_valid():
            cat = form_cat.save(commit=True)
            bytes_io = to_thumbnail(cat.photo)
            cat.thumbnail.save(name=f'thumbnail-image-{cat.id}.jpg', content=bytes_io, save=True)

            return redirect('cats:detail', pk=pk)
    else:
        form_cat = FormCat(instance=cat)

    photo_url = cat.photo.url if cat.photo else None
    context = dict(form_cat = form_cat, pk=pk, photo_url=photo_url)
    return render(request, 'cats/update.html', context)


def delete_view(request,pk):
    cat = Cat.objects.get(id=pk)
    cat.delete()
    return redirect('cats:list')