from django import forms
from .models import User

class FileFieldForm(forms.Form)::
    label = ""
    class Meta:
        model = User
        fields = ('media')
        file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': 
True}))
    