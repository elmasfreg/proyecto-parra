from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	avatar=models.ImageField(upload_to='Profiles',null=True,blank=True)
	bio=models.TextField(null=True,blank=True)
	Cumple=models.DateField(null=True)
@receiver(post_save,sender=User)
def ensure_profile_exists(sender,instance,**kwargs):
	if kwargs.get('created',False):
		Profile.objects.get_or_create(user=instance)
		print("se acaba de crear un usuario y su perfil enlazado")