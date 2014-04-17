from django.db import models

class InscritoExpo(models.Model):
	dni = models.CharField(max_length=8,verbose_name='DNI')
	nombres = models.CharField(max_length=120,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=120,verbose_name='Apellidos')
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Tel-Cel')
	organizacion = models.CharField(max_length=200)
	pago = models.FloatField(null=True,blank=True)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	fecha_edicion = models.DateTimeField(auto_now=True)
	certificado = models.BooleanField(default=False)
	asistencia = models.BooleanField(default=False)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

	class Meta:
		ordering = ['-fecha_registro']

class Colaborador(models.Model):
	dni = models.CharField(max_length=8,verbose_name='DNI')
	nombres = models.CharField(max_length=120,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=120,verbose_name='Apellidos')
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Telefono - Celular')
	organizacion = models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
	colabora = models.TextField(verbose_name='En que quiere colaborar')

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

	class Meta:
		ordering = ['-fecha']

class Ponente(models.Model):
	dni = models.CharField(max_length=8,verbose_name='DNI')
	nombres = models.CharField(max_length=120,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=120,verbose_name='Apellidos')
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Telefono - Celular')
	organizacion = models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
	ponencia = models.TextField(verbose_name='Tema de la ponencia')

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

	class Meta:
		ordering = ['-fecha']

class Auspiciador(models.Model):
	nombre = models.CharField(max_length=120)
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Telefono - Celular')
	fecha = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
	auspicio = models.TextField(verbose_name='Con que aporto')

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ['-fecha']

class Taller(models.Model):
	nombre = models.CharField(max_length=120,verbose_name='Taller')
	precio = models.FloatField(null=True,blank=True)
	ponente = models.ForeignKey(Ponente)

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ['-nombre']

class InscritoTaller(models.Model):
	dni = models.CharField(max_length=8,verbose_name='DNI')
	nombres = models.CharField(max_length=120,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=120,verbose_name='Apellidos')
	email = models.EmailField(max_length=200,verbose_name='E-Mail')
	telefono = models.CharField(max_length=15,verbose_name='Tel-Cel')
	organizacion = models.CharField(max_length=200)
	pago = models.FloatField(null=True,blank=True)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	fecha_edicion = models.DateTimeField(auto_now=True)
	certificado = models.BooleanField(default=False)
	asistencia = models.BooleanField(default=False)
	taller = models.ForeignKey(Taller)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

	class Meta:
		ordering = ['-fecha_registro']