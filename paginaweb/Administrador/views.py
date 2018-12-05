from django.shortcuts import render,get_object_or_404,redirect
from .models import ProjectManager,Project,Tareas
from .forms import ProyectForm,TareaForm,EquipoForm,AgregarIntegrantesForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from Developer.models import Team,DevTeam
# Create your views here.
class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_staff:
			return redirect(reverse_lazy('login'))
		if request.user.id!=1:
			return redirect(reverse_lazy('Developer:indexusuario'))
		return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
	
class homeListView(StaffRequiredMixin,ListView):
	model=Project

class TareasListView(ListView):
	model=Tareas
	
       

class ProyectosCrear(StaffRequiredMixin,CreateView):
	model = Project
	form_class=ProyectForm
	#fields=['Id_Manager','Teamforproject','ProjectName','Company','about','DeadLine']

	def get_success_url(self):
		return reverse('Administrador:home')



class ProyectoUpdate(StaffRequiredMixin,UpdateView):
	model=Project
	form_class=ProyectForm
	template_name_suffix='_update_form'

	def get_success_url(self):
		return reverse_lazy('Administrador:revisar',args=[self.object.id_Project])

class TareaCrear(CreateView):
	model=Tareas
	form_class=TareaForm
	#fields=['id_Dev','id_Proj','Name','about','DeadLine']
	def get_success_url(self):
		return reverse('Administrador:home')
class EquipoCrear(CreateView):
	form_class=EquipoForm
	template_name='Administrador/crearEquipos.html'

	def get_success_url(self):
		return reverse('Administrador:CrearEquipo')

class ProjectDelete(StaffRequiredMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('Administrador:home')	
class UpdateTareas(UpdateView):
	model=Tareas
	form_class=TareaForm
	template_name="Administrador/actualizartareas.html"
	def get_success_url(self):
		return reverse_lazy('Administrador:TareasDeProyecto',args=[self.object.id_Proj.id_Project])

class DeleteTareas(DeleteView):
	model=Tareas
	def get_success_url(self):
		return reverse_lazy('Administrador:TareasDeProyecto',args=[self.object.id_Proj.id_Project])
class CrearTeam(CreateView):
	form_class=AgregarIntegrantesForm
	template_name="Administrador/agregarintegrantes.html"
	
	def get_success_url(self):
		return reverse_lazy('Administrador:CrearEquipo')
class TeamList(ListView):
	model =Team
	template_name='Administrador/verequipos.html'

def home(request):
	projectmanager=ProjectManager.objects.all()
	return render(request,"Administrador/home.html",{"projectmanager":projectmanager})

def proyectos(request):
	proyect_form=ProyectForm()
	projects=Project.objects.all()
	return render(request, "Administrador/proyectos.html",{"proyects":projects,"form":proyect_form})


def tareas(request):

	return render(request,"Administrador/tareas.html")


class revisarDetailView(StaffRequiredMixin,DetailView):
	model=Project

class TareasDeProyectoListView(ListView):
	model=Tareas
	
def TareasDeProyecto(request,tareas):

	task=Tareas.objects.filter(id_Proj=tareas)

	return render(request,'Administrador/tareasdeproyecto.html',{"task":task})


def base(request):
	project=Project.objects.all()
	#query=Tareas.objects.all()
	return render(request,"Administrador/base.html",{"project":project})

def detalleproyecto(request,detalle_id):
	detalle=get_object_or_404(Project,id_Project=detalle_id)
	task= get_object_or_404(Tareas,id_Proj=detalle_id)
	#tareas=get_object_or_404(Project,id_Project='1')
	return render(request,'Administrador/detalleproyecto.html',{"detalle":detalle,"task":task})
def integrantesEqupo(request,id):

	team=DevTeam.objects.filter(idTeam=id)

	return render(request,'Administrador/integrantesequipo.html',{"team":team})