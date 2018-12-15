from django import forms
from .models import Car, CarImage


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', 'images')
    
    imgs = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple": True}))
