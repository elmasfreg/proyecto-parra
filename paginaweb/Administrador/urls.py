"""paginaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
"""from Administrador import views as Admin_views"""
from . import views
from .views import homeListView,revisarDetailView,ProyectosCrear,ProyectoUpdate,ProjectDelete,TareaCrear,EquipoCrear,TareasDeProyectoListView,UpdateTareas,DeleteTareas,CrearTeam,TeamList
Administrador_patterns = ([
    
    path('',homeListView.as_view(),name="home"),
    path('home/',views.home,name="home2"),
    path('proyectos/',views.proyectos,name="proyectos2"),
  #  path('tareas/',views.tareas,name="tareas"),
     path('revisar/<int:pk>/',revisarDetailView.as_view(),name="revisar"),
    path('detalleproyecto/<int:detalle_id>/',views.detalleproyecto,name="detalleproyecto"),
    path('CrearProyectos/',ProyectosCrear.as_view(),name="proyectos"),
    path('ActualizarProyectos/<int:pk>/',ProyectoUpdate.as_view(),name="ActualizarProyectos"),
    path('ActualizarTareas/<int:pk>/',UpdateTareas.as_view(),name="UpdateTareas"),
    path('BorrarProyectos/<int:pk>/',ProjectDelete.as_view(),name="BorrarProyectos"),
    path('BorrarTareas/<int:pk>/',DeleteTareas.as_view(),name="BorrarTareas"),
    path('CrearTarea/',TareaCrear.as_view(),name="tareas"),
    path('CrearEquipo/',EquipoCrear.as_view(),name="CrearEquipo"),
    path('tareasproyecto/<int:tareas>/',views.TareasDeProyecto,name="TareasDeProyecto"),
    path('AgregarIntegrantes/',CrearTeam.as_view(),name="AgregarIntegrantes"),
    path('VerEquipos/',TeamList.as_view(),name="VerEquipos"),
    path('VerIntegrantes/<int:id>/',views.integrantesEqupo,name="VerIntegrantes"),

],'Administrador')