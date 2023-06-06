# Generated by Django 4.1.6 on 2023-06-04 10:20

import diploma.validator
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diploma', '0018_delete_category_delete_confirm_remove_employer_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Confirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='files_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Тема документа', max_length=280)),
                ('file', models.FileField(upload_to='document/', validators=[diploma.validator.validate_file_size])),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(default='uncategorized', help_text='Категория', max_length=280)),
                ('date_confirm', models.CharField(help_text='Дата утверждения', max_length=300, null=True)),
                ('confirm', models.CharField(blank=True, default='Действующий документ', max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('birthday', models.DateField(help_text='Введите дату рождения в указаном формате: ГГГГ-ММ-ДД', null=True)),
                ('email', models.CharField(help_text='Ведите электронную почту', max_length=100, null=True)),
                ('phone', models.CharField(help_text='8 7** *** ****', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
