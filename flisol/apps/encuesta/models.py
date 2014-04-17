from django.db import models
from flisol.apps.home.models import UserProfile

class Encuesta(models.Model):
	titulo = models.CharField(max_length=120,verbose_name='Titulo de la Encuesta')
	descripcion = models.TextField(verbose_name='Descripcion de la Encuesta')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	userProfile = models.ForeignKey(UserProfile,verbose_name='Usuario')

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-fecha_creacion']

class Pregunta(models.Model):
	formulacion = models.CharField(max_length=250,verbose_name='Pregunta')
	obligatoria = models.BooleanField(default=True)
	encuesta = models.ForeignKey(Encuesta,verbose_name='Encuesta')

	def __unicode__(self):
		return self.formulacion

	class Meta:
		ordering = ['-encuesta']

class Opcion(models.Model):
	opcion = models.CharField(max_length=300)
	votos = models.IntegerField(null=True,blank=True)
	pregunta = models.ForeignKey(Pregunta,verbose_name='Pregunta')

	def __unicode__(self):
		return self.opcion

	class Meta:
		ordering = ['-pregunta']

class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length=120,verbose_name='Nombre del Grupo')

	def __unicode__(self):
		return self.nombre_grupo

class Asignacion(models.Model):
	fecha_inicio = models.DateTimeField(auto_now_add=True,editable=True,blank=True)
	fecha_finalizacion = models.DateTimeField(auto_now=True,editable=False,blank=True)
	activo = models.BooleanField(default=False)
	encuesta = models.ForeignKey(Encuesta)
	grupo = models.ForeignKey(Grupo)

	class Meta:
		ordering = ['-fecha_inicio']