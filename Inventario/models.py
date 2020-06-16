from django.db import models

# Create your models here.
class Valores_Atributo(models.Model):
	valor = models.CharField(max_length=255)

	class Meta:
		verbose_name = "Valor de Atributo"
		verbose_name_plural = "Valores de Atributos"

	def __str__(self):
		return self.valor

class Atributo(models.Model):
	nombre = models.CharField('Nombre del Atributo', max_length=255)
	valor = models.ManyToManyField(Valores_Atributo, related_name='ValorAtributo')
	class Meta:
		verbose_name = "Atributo"
		verbose_name_plural = "Atributos"

	def __str__(self):
		return self.nombre

class Variante(models.Model):
	valor = models.ForeignKey(
		Valores_Atributo,
		on_delete=models.CASCADE,
		related_name='ValorVariante',
		)
	precio_venta = precio_venta = models.DecimalField('Precio de Venta',max_digits=10, decimal_places=2)
	class Meta:
		verbose_name = "Variante"
		verbose_name_plural = "Variantes"

	def __str__(self):
		return self.valor.valor

class Producto(models.Model):
	nombre_producto = models.CharField('Nombre del Producto',max_length=255)
	vender = models.BooleanField('Se puede vender',default=True)
	comprar = models.BooleanField('Se puede comprar',default=True)
	TIPO_PRODUCTO_CHOICES = (
		('Co' , 'Consumible'), 
		('Se' , 'Servicio'), 
		('Al' , 'Almacenable'),
		)
	tipo_producto = models.CharField('Tipo de Producto',max_length=255, choices=TIPO_PRODUCTO_CHOICES, default='Al')
	codigo_barras = models.CharField('Codigo de Barras',max_length=255, null=True, blank=True)
	precio_venta = models.DecimalField('Precio de Venta',max_digits=10, decimal_places=2)
	coste = models.DecimalField('Coste', max_digits=10, decimal_places=2, default=0.00)
	peso = models.DecimalField('Peso', max_digits=4, decimal_places=2, default=0.00)
	volumen = models.DecimalField('Volumen', max_digits=4, decimal_places=2, default=0.00)
	descripcion = models.TextField('Descripcion', null=True, blank=True)
	foto = models.ImageField('Imagen del Producto', upload_to='fotos/producto/', null=True, blank=True)
	cantidad = models.PositiveIntegerField('Cantidad a Mano', default=0)
	capacidad = models.PositiveIntegerField('Capacidad de Produccion', default=0)
	caducidad = models.DateField('Fecha de Caducidad', null=True, blank=True)
	atributo = models.ManyToManyField(Atributo, blank=True, related_name='AtributoProducto')
	valores = models.ManyToManyField(Valores_Atributo, blank=True, related_name='ValoresProducto')

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"

	def __str__(self):
		return self.nombre_producto