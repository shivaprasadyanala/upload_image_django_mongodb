# forms.py
from django import forms
from .models import Test

class ImageForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['image_file']
