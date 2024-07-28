from cages.models import Cage
from django import forms

class FormCage(forms.ModelForm):
    class Meta:
        model = Cage
        fields = '__all__'
