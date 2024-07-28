from django.shortcuts import render, redirect
from colonies.forms import FormColony
from colonies.models import Colony

def list_view(request):

    context = dict(list_colony=Colony.objects.all())
    return render(request, 'colonies/list.html', context)


def create_view(request):

    if request.method == 'POST':
        form_colony = FormColony(data=request.POST)
        if form_colony.is_valid():
            form_colony.save()
            return redirect('colonies:list')
    else:
        form_colony = FormColony()
        
    context = dict(
        form_colony = form_colony,
    )
    return render(request, 'colonies/create.html', context)


def detail_view(request,pk):
    colony = Colony.objects.get(id=pk)
    context = dict(colony=colony)
    return render(request, 'colonies/detail.html', context)


def update_view(request,pk):
    colony = Colony.objects.get(id=pk)

    if request.method == 'POST':
        form_colony = FormColony(data=request.POST, instance=colony)
        if form_colony.is_valid():
            colony = form_colony.save()
            return redirect('colonies:detail', pk=pk)
    else:
        form_colony = FormColony(instance=colony)

    # thumbnail_url = colony.thumbnail.url if colony.thumbnail else None
    # context = dict(form_colony = form_colony, pk=pk, thumbnail_url=thumbnail_url)
    context = dict(form_colony = form_colony, pk=pk)
    return render(request, 'colonies/update.html', context)


def delete_view(request,pk):
    colony = Colony.objects.get(id=pk)
    colony.delete()
    return redirect('colonies:list')