from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ('nombre_producto', 'vender', 'comprar', 'precio_venta', 'variante', 'tipo_producto', 'codigo_barras', 
			'coste', 'peso', 'volumen', 'descripcion', 'foto', 'cantidad', 'capacidad', 'caducidad')
