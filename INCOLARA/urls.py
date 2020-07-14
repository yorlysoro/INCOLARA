from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from Base.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', login_required(Inicio.as_view()), name='inicio'),
    path('base/', include('Base.urls')),
    path('inventario/', include('Inventario.urls')),
    path('', include('allauth.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
