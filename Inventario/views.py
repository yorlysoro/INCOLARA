from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DetailView, DeleteView
from .models import Producto
from .forms import ProductoForm
# Create your views here.

class ListaProductos(ListView):
	model = Producto
	template_name = 'Inventario/producto/list_productos.html'
	context_object_name = 'Productos'


class DetalleProducto(DetailView):
	model = Producto
	template_name = 'Inventario/producto/detalle_producto.html'
	context_object_name = 'Producto'

class CrearProducto(CreateView):
	model = Producto
	template_name = 'Inventario/producto/crear_producto.html'
	form_class = ProductoForm


class ActualizarProducto(UpdateView):
	model = Producto
	template_name = 'Inventario/producto/modificar_producto.html'
	form_class = ProductoForm


class BorrarProducto(DeleteView):
	model = Producto
	template_name = 'Inventario/producto/borrar_producto.html'

