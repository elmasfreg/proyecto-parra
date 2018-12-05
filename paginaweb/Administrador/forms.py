from django import forms
from .models import Project,Tareas
from Developer.models import Team,DevTeam
class ProyectForm(forms.ModelForm):

	class Meta:

		model=Project
		fields=['Id_Manager','Teamforproject','ProjectName','Company','about','DeadLine']
		widgets={ 
		'Id_Manager':forms.Select(attrs={'class':'form-control col-lg-12','value':''}),
		'Teamforproject':forms.Select(attrs={'class':'form-control col-lg-12'}),
		'ProjectName':forms.TextInput(attrs={'class':'form-control col-lg-12'}),
		'Company':forms.TextInput(attrs={'class':'form-control col-lg-12'}),
		'about':forms.Textarea(attrs={'class':'form-control col-lg-12'}),
		'DeadLine':forms.TextInput(attrs={'class':'form-control col-lg-12','type':'date'}),
		}

class TareaForm(forms.ModelForm):
	class Meta:
		model= Tareas
		fields=['id_Dev','id_Proj','Name','about','DeadLine']
		widgets={
		'id_Dev':forms.Select(attrs={'class':'form-control col-lg-12'}),
		'id_Proj':forms.Select(attrs={'class':'form-control col-lg-12'}),
		'Name':forms.TextInput(attrs={'class':'form-control'}),
		'about':forms.Textarea(attrs={'class':'form-control'}),
		'DeadLine':forms.TextInput(attrs={'class':'form-control col-lg-12','type':'date'}),
		}

class EquipoForm(forms.ModelForm):
	class Meta:
		model=Team
		fields=['TeamName']
		widgets={
		'TeamName':forms.TextInput(attrs={'class':'form-control col-lg-12' }),
		}
class AgregarIntegrantesForm(forms.ModelForm):
	class Meta:
	
		model=DevTeam
		fields=['idDev','idTeam']
		widgets={
		'idDev':forms.Select(attrs={'class':'form-control col-lg-12'}),
		'idTeam':forms.Select(attrs={'class':'form-control col-lg-12'}),
		}