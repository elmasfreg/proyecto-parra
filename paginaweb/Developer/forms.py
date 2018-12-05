from django import forms
from Administrador.models import Project,Tareas
from .models import Team,DevTeam

class TareaFormdev(forms.ModelForm):
	class Meta:
		model= Tareas
		fields=['Name','about']
		widgets={
		'Name':forms.TextInput(attrs={'class':'form-control'}),
		'about':forms.Textarea(attrs={'class':'form-control'}),
		}