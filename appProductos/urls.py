from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.verCategorias, name='categorias'), 
    path('productos/<int:idCateg>', views.verProductosCategoria, name='prodCategoria'), 
    path('detalle/<int:idProd>', views.verDetalleProducto, name='detalle'), 
    path('agregar_carro/<int:idProd>', views.agregarCarro, name='agregarCarro'), 
    path('carrito/', views.verCarrito, name='carrito'), 

]