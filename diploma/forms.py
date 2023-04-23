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

choices = Category.objects.all().values_list('name', 'name')

class FilesForm(forms.ModelForm):
    class Meta:
        model = files_doc
        fields = ['topic', 'file', 'category', 'date_confirm']
        widgets = {
            'category' : forms.Select(choices=choices, attrs={'class' : 'form-control, col-xl-4'}),
        }

