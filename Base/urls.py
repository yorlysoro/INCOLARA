from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SectoresListar, SectoresCrear, SectoresEditar, SectoresDetalle, SectoresBorrar,  MiCuenta

app_name = 'Base'
urlpatterns = [
	path('mi_cuenta/', login_required(MiCuenta.as_view()), name='mi_cuenta'),
    path('lista_sectores/', login_required(SectoresListar.as_view()), name='lista_sectores' ),
    path('sector_crear/', login_required(SectoresCrear.as_view()), name='sector_crear'),
    path('sector_editar/<int:pk>', login_required(SectoresEditar.as_view()), name='sector_editar'),
    path('sector_detalle/<int:pk>', login_required(SectoresDetalle.as_view()), name='sector_detalle'),
    path('sector_borrar/<int:pk>', login_required(SectoresBorrar.as_view()), name='sector_borrar'),
]