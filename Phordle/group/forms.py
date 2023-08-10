from django import forms

from .models import Group

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ["name"]

class AddUserForm(forms.ModelForm):
    add_user = forms.CharField()

    class Meta:
        model = Group
        fields = []