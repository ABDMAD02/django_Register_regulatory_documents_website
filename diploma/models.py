from django.db import models
from django.contrib.auth.models import User
from .validator import validate_file_size

# Create your models here.

class employer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,  null=True)
    surname = models.CharField(max_length=200,  null=True)
    birthday = models.DateField(help_text='Введите дату рождения в указаном формате: ГГГГ-ММ-ДД',  null=True)
    email = models.CharField(max_length=100, help_text='Ведите электронную почту',  null=True)
    phone = models.CharField(max_length=200, null=True, help_text='8 7** *** ****')
    profile_img = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.name 
    
class files_doc(models.Model):
    topic = models.CharField(max_length=280, help_text='Тема документа')
    file = models.FileField(upload_to='document/', validators=[validate_file_size])
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True )
    category = models.CharField(max_length=280, default='uncategorized', help_text='Категория')
    date_confirm = models.CharField(max_length=300, help_text='Дата утверждения', null=True)
    confirm = models.CharField(max_length=280, default='Действующий документ', blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.topic 

class Category(models.Model):
    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name
    
class Confirm(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

