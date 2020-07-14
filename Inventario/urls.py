from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaProductos, DetalleProducto, CrearProducto, ActualizarProducto, BorrarProducto

app_name = 'Inventario'
urlpatterns = [
	path('lista_productos/', login_required(ListaProductos.as_view()), name='lista_productos'),
	path('detalle_producto/<int:pk>/', login_required(DetalleProducto.as_view()), name='detalle_producto'),
]