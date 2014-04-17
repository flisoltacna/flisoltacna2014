from django.contrib import admin
from flisol.apps.encuesta.models import Encuesta,Pregunta,Opcion,Grupo,Asignacion

class EncuestaAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha_creacion','userProfile')
	search_fields = ['titulo']
	fields = ('titulo','descripcion','userProfile')

class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('formulacion','obligatoria')
	list_filter = ('obligatoria','encuesta')
	search_fields = ['formulacion']
	fields = ('formulacion','obligatoria','encuesta')

class OpcionAdmin(admin.ModelAdmin):
	list_display = ('opcion','pregunta','votos')
	search_fields = ['pregunta']
	fields = ('pregunta','opcion','votos')

class AsignacionAdmin(admin.ModelAdmin):
	list_display = ('fecha_inicio','fecha_finalizacion','activo','encuesta')
	list_filter = ('activo','encuesta','grupo')
	search_fields = ['activo','encuesta','grupo']
	fields = ('encuesta','grupo','activo')

admin.site.register(Encuesta,EncuestaAdmin)
admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Opcion,OpcionAdmin)
admin.site.register(Grupo)
admin.site.register(Asignacion,AsignacionAdmin)