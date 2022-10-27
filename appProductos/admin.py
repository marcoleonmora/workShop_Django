from django.contrib import admin
from .models import *

# Register your models here.

#---------------------------------------------
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','descripCategoria']

admin.site.register(Categoria, CategoriaAdmin)

#---------------------------------------------
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','imgGrande', 'imgPeque']

admin.site.register(Producto, ProductoAdmin)

#---------------------------------------------
class CarroAdmin(admin.ModelAdmin):
    list_display = ['usuario','producto', 'cantidad', 'estado']

admin.site.register(Carro, CarroAdmin)

