from django.contrib import admin
from flisol.apps.home.models import UserProfile,Publicacion

class UserAdmin(admin.ModelAdmin):
	list_display = ('user','telefono')
	search_fields = ['user']
	fields = ('user','telefono')

class PublicacionAdmin(admin.ModelAdmin):
	list_display = ('titulo','thumbnail','fecha_registro','fecha_edicion','userProfile')
	list_filter = ('userProfile',)
	search_fields = ['titulo']
	fields = ('titulo','descripcion','imagen','userProfile','etiquetas')

admin.site.register(UserProfile,UserAdmin)
admin.site.register(Publicacion,PublicacionAdmin)