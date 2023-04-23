from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class employer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,  null=True)
    surname = models.CharField(max_length=200,  null=True)
    birthday = models.DateField(help_text='Enter birthday in the following format: YYYY-MM-DD',  null=True)
    email = models.CharField(max_length=100, help_text='Enter your corporate email',  null=True)
    position = models.CharField(max_length=200, help_text='Your responsibilities',  null=True)
    phone = models.CharField(max_length=200, null=True, help_text='8 7** *** ****')
    profile_img = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.name 
    
class files_doc(models.Model):
    topic = models.CharField(max_length=280, help_text='Тема документа')
    file = models.FileField(upload_to='document/pdf')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True )
    category = models.CharField(max_length=280, default='uncategorized', help_text='Категория')
    date_confirm = models.CharField(max_length=300, help_text='Дата утверждения', null=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.topic 

class Category(models.Model):
    name = models.CharField(max_length=280)

    def __str__(self):
        return 'Obj: {}'.format(self.id)

    # def __str__(self):
    #     return self.name

 

