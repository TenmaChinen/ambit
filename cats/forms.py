from cats.models import Cat, CatPicture
from django import forms


class FormCat(forms.ModelForm):

    class Meta:
        model = Cat
        exclude = ('pictures','thumbnail')
        widgets = {
            'photo': forms.FileInput(attrs={'style': 'display:none;'}),
            'sterlize_date': forms.DateInput(attrs={'type': 'date'}),
            'sighting_date': forms.DateInput(attrs={'type': 'date'}),
        }


T_STERILIZED_CHOICES = ( (None,'----'), (True, 'Sí'), (False, 'No') )

class FormCatFilter(forms.ModelForm):

    sterilized = forms.ChoiceField(choices=T_STERILIZED_CHOICES, initial=True, required=False, label='Esterilizado')

    class Meta:
        model = Cat
        exclude = ('photo','thumbnail','pictures','sighting_date','sterlize_date','record_date')
        # fields = ('colony','gender','sterilized','frequency','state','sociability')

# class FormCatPicture(forms.ModelForm):

#     class Meta:
#         model = CatPicture
#         fields = ('image',)
#         widgets = {
#             'image': forms.FileInput(attrs={'style': 'display:none;'}),
#         }