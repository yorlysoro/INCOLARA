from django.contrib import admin
from .models import Producto, Variante, Atributo, Valores_Atributo
# Register your models here.


admin.site.register(Producto)
admin.site.register(Variante)
admin.site.register(Atributo)
admin.site.register(Valores_Atributo)