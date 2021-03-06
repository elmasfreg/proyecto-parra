# Generated by Django 2.1 on 2018-12-05 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Developer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id_Project', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Proyecto')),
                ('ProjectName', models.CharField(max_length=200)),
                ('Company', models.CharField(max_length=200)),
                ('about', models.TextField(verbose_name='Acerca de')),
                ('DeadLine', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Id_Manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('Teamforproject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Developer.Team', verbose_name='Id del Equipo')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('IdManager', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('Name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('CumpleAños', models.DateTimeField(verbose_name='Cumple años')),
                ('status', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='Admin')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Administradore',
                'verbose_name_plural': 'Administradores',
            },
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id_Task', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Tarea')),
                ('Name', models.CharField(max_length=200)),
                ('about', models.TextField(verbose_name='Acerca de')),
                ('DeadLine', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id_Dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id Programador')),
                ('id_Proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Project', verbose_name='Id del proyecto')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
