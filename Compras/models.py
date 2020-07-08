from django.db import models
from Base.models import Cuenta
from  Ventas.models import Venta, Subasta
# Create your models here.
class Orden_Compra(models.Model):
	usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='Cuenta_Orden_Compra')
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	class Meta:
		verbose_name = "Orden de Compra"
		verbose_name_plural = "Ordenes de Compra"

	def __str__(self):
		return self.cantidad + " de " + self.venta.titulo

class Orden(models.Model):
	usuario= models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='Cuenta_Orden')
	ref_code = models.CharField('Codigo de Referencia',max_length=20, blank=True, null=True)
	productos = models.ManyToManyField(Orden_Compra)
	fecha_orden = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = "Orden"
		verbose_name_plural = "Ordenes"
	def __str__(self):
		self.usuario.username

class Subastar(models.Model):
	usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='Cuenta_Subastar')
	subasta = models.ForeignKey(Subasta, null=True, blank=True, on_delete=models.SET_NULL)
	precio_subasta = models.DecimalField('Precio a Subastar',  max_digits=10, decimal_places=2, default=0.00)
	descripcion = models.TextField('Nota/Descripcion', null=True, blank=True)
	class Meta:
		verbose_name = "Subastar"
		verbose_name_plural = "Subastar"
	def __str__(self):
		return self.usuario.username + " en " + self.subasta.titulo