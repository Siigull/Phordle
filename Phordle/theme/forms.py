from django import forms

from .models import Theme
from feed.models import Image

class ThemeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter theme name'}))
    public = forms.BooleanField()

    class Meta:
        model = Theme
        fields = ["name", "public", "word_0", "word_1", "word_2"]

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ["image"]
