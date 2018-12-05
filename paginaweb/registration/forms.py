from django import forms
from .models import Profile
from django.contrib.auth.models import User
class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields =['avatar','bio','Cumple']
		widgets={
			'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'bio':forms.Textarea(attrs={'class':'form-control mt-3','rows':3,'placeholder':'Biografia'}),
			'Cumple':forms.TextInput(attrs={'class':'form-control ','type':'date'}),
		}

class EmailForm(forms.ModelForm):
	email = forms.EmailField(required=True,help_text="Rquerido. 254 caracteres como maximo y debe ser valido.")

	class Meta:
		model=User
		fields=['email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if 'email' in self.changed_data:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError("El email ya esta registrado, prueba con otro-")
		return email
