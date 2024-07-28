from colonies.models import Colony
from django import forms

class FormColony(forms.ModelForm):
    class Meta:
        model = Colony
        fields = '__all__'