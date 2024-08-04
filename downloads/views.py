from django.shortcuts import render, redirect
from downloads.forms import FormCensus
from django.http import FileResponse
# from colonies.models import Colony
from colonies.models import Colony
from downloads import utils
from io import BytesIO
import pdb

def download_census(request):
	if request.method == 'POST':
		form_census = FormCensus(data=request.POST)
		if form_census.is_valid():
			d_census = form_census.cleaned_data
			colony = d_census['colony']
			buffer = utils.create_census_pdf(colony_id=colony.id)
			colony_name = colony.name.lower()
			return FileResponse(buffer, as_attachment=True, filename=f'censo_{colony_name}.pdf')