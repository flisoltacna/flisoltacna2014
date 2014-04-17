from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,verbose_name='Usuario')
	telefono = models.CharField(max_length=15)
	
	def __unicode__(self):
		return self.user.username

class Publicacion(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Publicacion/%s/%s"%(self.titulo,str(filename))
		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True

	titulo = models.CharField(max_length=120,verbose_name='Titulo de la Publicacion')
	descripcion = models.TextField(verbose_name='Contenido de la publicacion')
	imagen = models.ImageField(upload_to=url,null=True,blank=True)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	fecha_edicion = models.DateTimeField(auto_now=True)
	etiquetas = models.CharField(max_length=225,null=True,blank=True)
	userProfile = models.ForeignKey(UserProfile,verbose_name='Usuario')

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-fecha_registro']