from django import forms
from .models import Neighborhood,Business

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        exclude=['user','occupants_count']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user']
