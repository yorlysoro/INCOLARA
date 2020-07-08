from django.db import models
from Base.models import Cuenta
from Inventario.models import Producto, Variante
# Create your models here.

class Base(models.Model):
	titulo = models.CharField('Titulo', max_length=255)
	info_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	variante = models.ForeignKey(Variante, on_delete=models.CASCADE)
	precio = models.DecimalField('Precio',  max_digits=10, decimal_places=2, default=0.00)
	nota = models.TextField('Nota/Descripcion', null=True, blank=True)
	fecha_publicacion = models.DateField('Fecha de Publicacion', auto_now_add=True)
	fecha_modificacion = models.DateField('Fecha de Modificacion', auto_now=True)

	class Meta:
		abstract = True

class Venta(Base):
	usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None, related_name='Venta_Cuenta')
	class Meta:
		verbose_name = "Venta"
		verbose_name_plural = "Ventas"

	def __str__(self):
		return self.titulo

class Subasta(Base):
	usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None, related_name='Subasta_Cuenta')
	inicio = models.DateField('Fecha de Apertura')
	final = models.DateField('Fecha de Culminacion')
	
	class Meta:
		verbose_name = "Subasta"
		verbose_name_plural = "Subastas"

	def __str__(self):
		return self.titulo

#class Oferta(models.Model):
#	pass