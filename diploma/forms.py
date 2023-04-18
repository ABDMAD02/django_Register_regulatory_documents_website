from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployerForm(ModelForm):
    class Meta:
        model = employer 
        fields = '__all__'
        exclude = ['user']

class FilesForm(forms.ModelForm):
    class Meta:
        model = pdf_files
        fields = ['topic', 'pdf_file']