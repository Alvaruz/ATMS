from django.db import models
from django.utils import timezone

class Equipos(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	
	def __str__(self):
		return self.nombre


class Stock(models.Model):
	nombre = models.ForeignKey(Equipos, on_delete=models.CASCADE)
	buenos = models.IntegerField()
	dañados = models.IntegerField()

	def __str__(self):
		return self.nombre


class Grupo(models.Model):
	nombre = models.CharField(max_length=25)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


class Usuario(models.Model):
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	grupo = models.ManyToManyField(Grupo)

	def __str__(self):
		return self.nombre


class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	relevancia = models.CharField(max_length=30, null=True)

	def __str__(self):
		return self.nombre

class Estado(models.Model):
	nombre= models.CharField(max_length=30)
	descripcion = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.nombre


class Ticket(models.Model):

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	ubicacion = models.CharField(max_length=50)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
	grupo_destino = models.ForeignKey(Grupo, on_delete=models.CASCADE,null=True, blank=True)
	detalle = models.TextField()
	equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, null=True, blank=True)
	fecha = models.DateTimeField(default=timezone.now, null=True, blank=True)
	estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)

	# editado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='nombre')
	editado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='nombre2', null=True, blank=True)
	fecha_fin = models.DateTimeField(null=True, blank=True)
	codigo = models.CharField(max_length=20, null=True, blank=True)
	imagen = models.ImageField(null=True, blank=True)

	def publicado_reciente(self):
		return self.fecha >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return '%s, %s' %(self.ubicacion, self.grupo_destino)


	# grupo_choices = (
	# 		('OPR','Operadores'),
	# 		('TEC','Tecnicos'),
	# 		('SIS','Sistemas'),
	# 		('PMT','PMT'),
	# 		('DOC','Administrativa'),
	# 	)