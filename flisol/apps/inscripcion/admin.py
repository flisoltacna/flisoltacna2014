from django.contrib import admin
from flisol.apps.inscripcion.models import InscritoExpo,InscritoTaller,Colaborador,Ponente,Auspiciador,Taller

class InscritoExpoAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','email','telefono','organizacion','fecha_registro','fecha_edicion','pago')
	list_filter = ('certificado','asistencia')
	search_fields = ['dni','apellidos','nombres']
	fields = (('nombres','apellidos'),('dni','telefono'),'email','organizacion',('certificado','asistencia'),'pago')

class InscritoTallerAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','email','telefono','organizacion','fecha_registro','fecha_edicion','pago')
	list_filter = ('certificado','asistencia','taller')
	search_fields = ['dni','apellidos','nombres']
	fields = (('nombres','apellidos'),('dni','telefono'),'email','organizacion',('certificado','asistencia'),('taller','pago'))

class TallerAdmin(admin.ModelAdmin):
	list_display = ('nombre','precio','ponente')
	search_fields = ['nombre']
	fields = ('nombre','precio','ponente')

class ColaboradorAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','email','organizacion','fecha')
	search_fields = ['dni','apellidos']
	fields = (('nombres','apellidos'),('dni','telefono'),'email','organizacion','colabora')

class PonenteAdmin(admin.ModelAdmin):
	list_display = ('dni','nombres','apellidos','email','organizacion','fecha')
	search_fields = ['dni','apellidos']
	fields = (('nombres','apellidos'),('dni','telefono'),'email','organizacion','ponencia')

class AuspiciadorAdmin(admin.ModelAdmin):
	list_display = ('nombre','email','telefono','fecha')
	search_fields = ['nombre']
	fields = ('nombre','email','telefono','auspicio')

admin.site.register(InscritoExpo,InscritoExpoAdmin)
admin.site.register(InscritoTaller,InscritoTallerAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(Colaborador,ColaboradorAdmin)
admin.site.register(Ponente,PonenteAdmin)
admin.site.register(Auspiciador,AuspiciadorAdmin)