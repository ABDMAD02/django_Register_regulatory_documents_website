# Generated by Django 4.1.6 on 2023-06-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diploma', '0016_alter_files_doc_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='position',
        ),
        migrations.AlterField(
            model_name='employer',
            name='birthday',
            field=models.DateField(help_text='Введите дату рождения в указаном формате: ГГГГ-ММ-ДД', null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.CharField(help_text='Ведите электронную почту', max_length=100, null=True),
        ),
    ]
