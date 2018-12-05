from .models import Project
from django.contrib.auth.models import User
def ctx_proyect(request):
	ctx={'proj':Project.objects.all()}
	return ctx
def ctx_user(request):
	ctxuser={'usuario':User.objects.filter(username=request.user)}
	return ctxuser
