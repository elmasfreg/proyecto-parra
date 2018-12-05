from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Developer(models.Model):
	id_Developer=models.AutoField(primary_key=True,verbose_name="id Usuario")
	id_DevTeam=models.IntegerField(verbose_name="Id Team",null=True)
	DevName=models.CharField(max_length=250,verbose_name="Nombre",null=True)
	Email=models.EmailField(verbose_name="Correo",null=True)
	BirthDate=models.DateField(auto_now=True,verbose_name="Fecha de Cumple Años",null=True)
	Password=models.CharField(max_length=250,null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)

	class Meta:
		verbose_name="Programador"
		verbose_name_plural="Programadores"
		ordering=["-created"]

	def __str__(self):
		return self.DevName;

class Team(models.Model):
	id_Team=models.AutoField(primary_key=True,verbose_name="id del equipo")
	TeamName=models.CharField(max_length=250,verbose_name="Nombre del equipo",null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)

	class Meta:
		verbose_name="Equipo"
		verbose_name_plural="Equipos"
		ordering=["-created"]

	def __str__(self):
		return self.TeamName;	

class DevTeam(models.Model):
	name=models.CharField(max_length=250,verbose_name="Nombre del equipo",null=True)
	idDev=models.ForeignKey(User,verbose_name="Id del Programador",on_delete=models.CASCADE,null=True)
	idTeam=models.ForeignKey(Team,verbose_name="Id del Equipo",on_delete=models.CASCADE,null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)
	class Meta:
		verbose_name="Equipo-Programador"
		verbose_name_plural="Equipos-Programadores"
		ordering=["-created"]

	def __str__(self):
		return self.name