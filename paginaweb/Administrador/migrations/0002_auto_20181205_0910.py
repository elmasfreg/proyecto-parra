# Generated by Django 2.1 on 2018-12-05 09:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='about',
            field=ckeditor.fields.RichTextField(verbose_name='Acerca de'),
        ),
    ]
