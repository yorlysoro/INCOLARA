from django.db import models
from django.contrib.auth.models import User
from Inventario.models import Producto, Variante
# Create your models here.

class Base(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	titulo = models.CharField('Titulo', max_length=255)
	info_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	variante = models.ForeignKey(Variante, on_delete=models.CASCADE)
	precio = models.DecimalField('Precio',  max_digits=10, decimal_places=2, default=0.00)
	nota = models.TextField('Nota/Descripcion', null=True, blank=True)

	class Meta:
		abstract = True

class Venta(Base):
	fecha_publicacion = models.DateField('Fecha de Publicacion', auto_now=True)
	class Meta:
		verbose_name = "Venta"
		verbose_name_plural = "Ventas"

	def __str__(self):
		return self.titulo

class Subasta(Base):
	inicio = models.DateField('Fecha de Apertura')
	final = models.DateField('Fecha de Culminacion')
	class Meta:
		verbose_name = "Subasta"
		verbose_name_plural = "Subastas"

	def __str__(self):
		return self.titulo

#class Oferta(models.Model):
#	pass