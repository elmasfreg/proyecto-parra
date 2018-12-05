from django.contrib import admin

from .models import ProjectManager,Project,Tareas
# Register your models here.
class ProjectManagerAdmin(admin.ModelAdmin):
	readonly_fields = ('IdManager','created','updated')

class ProjectAdmin(admin.ModelAdmin):
	readonly_fields = ('id_Project','created','updated')

class TareasAdmin(admin.ModelAdmin):
	readonly_fields = ('id_Task','created','updated')

class EquiposAdmin(admin.ModelAdmin):
	readonly_fields = ('id_Team','created','updated')

admin.site.register(ProjectManager,ProjectManagerAdmin),
admin.site.register(Project,ProjectAdmin),
admin.site.register(Tareas,TareasAdmin)
#admin.site.register(Team,EquiposAdmin)
