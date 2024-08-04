from django.shortcuts import render, redirect
from cats.forms import FormCat, FormCatFilter
from downloads.forms import FormCensus
from colonies.models import Colony
from django.urls import reverse
from cats.models import Cat
from cats import utils
import pdb


def create_view(request):

    if request.method == 'POST':
        form_cat = FormCat(data=request.POST, files=request.FILES)
        if form_cat.is_valid():
            form_cat.save(commit=True)
            return redirect('cats:list')
    else:
        d_query = request.session.get('query_cat',{})
        form_cat = FormCat(initial=d_query)

    context = dict(form_cat = form_cat)
    return render(request, 'cats/create.html', context)


def list_view(request):

    if request.GET:
        d_query = request.GET.dict()
        if 'filter' in d_query:
            del d_query['filter']
        request.session['query_cat'] = d_query
    else:
        d_query = request.session.get('query_cat',{})
        if 'filter' in d_query:
            del d_query['filter']

    form_cat_filter = FormCatFilter(data=d_query)
    
    d_query = {k: v for k, v in d_query.items() if v}
    
    if 'name' in d_query:
        d_query['name__contains'] = d_query.pop('name')

    records = Cat.objects.filter(**d_query)
    records = records.order_by('frequency', 'name')
    
    context = dict(
        list_cat=records,
        form_cat_filter=form_cat_filter,
        form_census=FormCensus(initial={'colony' : d_query.get('colony')})
    )
    
    if 'colony' in d_query:
        context['colony'] = Colony.objects.get(id=d_query['colony'])

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
            form_cat.save(commit=True)
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