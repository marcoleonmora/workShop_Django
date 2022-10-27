from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def verCategorias(request):
    listaCategorias = Categoria.objects.all()
    context = {
        'titulo': 'LISTADO DE CATEGORIAS',
        'categorias': listaCategorias,
    }

    return render(request, 'productos/categorias.html', context)

def verProductosCategoria(request, idCateg):
    #consultar la tabla Producto
    listaProductos = Producto.objects.filter(categoria=idCateg)
    #crear contexto
    context = {
        'titulo': 'LISTADO DE PRODUCTOS POR CATEGORIA',
        'productos': listaProductos,
    }
    #renderizar
    return render(request, 'productos/productos.html', context)
