from django.contrib import admin
from .models import Orden_Compra, Orden, Subastar
# Register your models here.
admin.site.register(Orden_Compra)
admin.site.register(Orden)
admin.site.register(Subastar)