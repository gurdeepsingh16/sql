from django import forms
from .models import *

class User_register(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ['last_login']
