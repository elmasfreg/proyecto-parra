from django.db import models
from django.contrib.auth.models import User
from Developer.models import Developer,Team
from ckeditor.fields import RichTextField
# Create your models here.
class ProjectManager(models.Model):
	IdManager=models.AutoField(primary_key=True,verbose_name="id")
	Name=models.CharField(max_length=200,verbose_name="Nombre")
	CumpleAños=models.DateTimeField(verbose_name="Cumple años")
	status=models.BooleanField()
	imagen=models.ImageField(upload_to="Admin")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name="Administradore"
		verbose_name_plural="Administradores"
		ordering=["-created"]
	def __str__(self):
		return self.Name

class Project(models.Model):
	id_Project=models.AutoField(primary_key=True,verbose_name="Id Proyecto")
	Id_Manager=models.ForeignKey(User,verbose_name="usuario",on_delete=models.CASCADE)
	Teamforproject=models.ForeignKey(Team,verbose_name="Id del Equipo",on_delete=models.CASCADE,null=True)
	ProjectName=models.CharField(max_length=200)
	Company=models.CharField(max_length=200)
	about =models.TextField(verbose_name="Acerca de")
	DeadLine=models.DateField(auto_now=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name="Proyecto"
		verbose_name_plural="Proyectos"
		ordering=["-created"]

	def __str__(self):
		return self.ProjectName

class Tareas(models.Model):
	id_Task=models.AutoField(primary_key=True,verbose_name="Id Tarea")
	id_Dev=models.ForeignKey(User,verbose_name="Id Programador",on_delete=models.CASCADE)
	id_Proj=models.ForeignKey(Project,verbose_name="Id del proyecto",on_delete=models.CASCADE)
	Name=models.CharField(max_length=200)
	about =RichTextField(verbose_name="Acerca de")
	DeadLine=models.DateField(auto_now=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name="Tarea"
		verbose_name_plural="Tareas"
		ordering=["-created"]

	def __str__(self):
		return self.Name


