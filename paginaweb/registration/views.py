from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from .models import Profile
from django.contrib.auth.decorators import login_required 
from .forms import ProfileForm,EmailForm
from django import forms
# Create your views here.
class SignUpView(CreateView):
	form_class=UserCreationForm
	success_url=reverse_lazy('login')
	template_name='registration/signup.html'

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
	form_class=ProfileForm
	success_url=reverse_lazy('profile')
	template_name='registration/profile_form.html'

	def get_object(self):

		profile, created = Profile.objects.get_or_create(user=self.request.user)
		return profile

@method_decorator(login_required,name='dispatch')
class EmailUpdate(UpdateView):
	form_class=EmailForm
	success_url=reverse_lazy('profile')
	template_name='registration/profile_email_form.html'

	def get_object(self):

		return self.request.user

	def get_form(self,form_class=None):
		form = super(EmailUpdate,self).get_form()

		form.fields['email'].widget = forms.EmailInput(
			attrs={'class':'form-control mb-2','placeholder':'Correo'})
		return form