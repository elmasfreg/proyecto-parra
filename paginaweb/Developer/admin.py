from django.contrib import admin
from .models import Developer,Team,DevTeam
# Register your models here.
class DevTeamAdmin(admin.ModelAdmin):
	readonly_fields = ('idDev','idTeam','created','updated')
admin.site.register(Developer),
admin.site.register(Team),
admin.site.register(DevTeam,DevTeamAdmin)

