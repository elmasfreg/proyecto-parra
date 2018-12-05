from django.shortcuts import render
from .forms import TareaFormdev
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Administrador.models import Tareas
from .models import Team
from django.urls import reverse,reverse_lazy
# Create your views here.
class IndexListView(ListView):
	model=Tareas
	template_name='Developer/tareas_list.html'
def MostrarTareas(request):
	task=Tareas.objects.filter(id_Dev=request.user.id)
	return render(request,"Developer/tareas_list.html",{"task":task})
class ModificarTarea(UpdateView):
	model=Tareas
	form_class=TareaFormdev
	template_name='Developer/actualizarTask.html'
	def get_success_url(self):
		return reverse_lazy('Developer:indexusuario')