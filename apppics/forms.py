from django import forms
from .models import *

class FormImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []
        fields = ('image_name', 'image_description', 'image')