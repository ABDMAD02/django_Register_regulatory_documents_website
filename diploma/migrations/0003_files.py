# Generated by Django 4.1.6 on 2023-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma', '0002_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=280)),
            ],
        ),
    ]