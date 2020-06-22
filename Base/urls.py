from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SectoresListar, MiCuenta

app_name = 'Base'
urlpatterns = [
	path('mi_cuenta/', login_required(MiCuenta.as_view()), name='mi_cuenta'),
    path('lista_sectores/', login_required(SectoresListar.as_view()), name='lista_sectores' ),
]