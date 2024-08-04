from cats.models import Cat
from django import forms

class FormCensus(forms.ModelForm):

	class Meta:
		model = Cat
		fields = ('colony',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['colony'].empty_label=None