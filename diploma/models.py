from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class example(models.Model):
    name = models.CharField(max_length=200)
    launch_Date = models.DateField()
    ready_to_launch = models.BooleanField(default=True)

    def __str__(self):
        return str(self)

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
    
class pdf_files(models.Model):
    topic = models.CharField(max_length=280)
    pdf_file = models.FileField(upload_to='document/pdf')

    def delete(self, *args, **kwargs):
        self.pdf_file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.topic 
 

