# Generated by Django 4.1.6 on 2023-04-14 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diploma', '0005_employer_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdf_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=280)),
                ('pdf_file', models.FileField(upload_to='document/pdf')),
            ],
        ),
        migrations.DeleteModel(
            name='FileS',
        ),
        migrations.AlterField(
            model_name='employer',
            name='phone',
            field=models.CharField(help_text='8 7** *** ****', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='profile_img',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
