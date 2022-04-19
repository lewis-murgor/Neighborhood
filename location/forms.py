from django import forms
from .models import Neighborhood,Business,Post,Profile

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        exclude=['user','occupants_count','joins']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','date']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood']
