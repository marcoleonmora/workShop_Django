from django.shortcuts import render
from .models import *

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

def verDetalleProducto(request, idProd):
    #consultar el producto
    regProducto = Producto.objects.get(id=idProd)
    #crear contexto
    context = {
        'titulo': 'DETALLE DEL PRODUCTO',
        'producto': regProducto,
    }
    #renderizar
    return render(request, 'productos/producto.html', context)


def agregarCarro(request, idProd):
    regUsuario = request.user
    msj = None
    #leer reg del producto en Producto
    existe = Producto.objects.filter(id=idProd).exists()
    if existe:
        regProducto = Producto.objects.get(id=idProd)

        # si no existe en carrito:
        existe = Carro.objects.filter(producto=regProducto, estado= 'activo', usuario= regUsuario).exists()
        if existe:
            # instanciar un objeto de la clase Carrito
            regCarro = Carro.objects.get(producto=regProducto, estado= 'activo', usuario= regUsuario)
            #incrementar cantidad
            regCarro.cantidad += 1
        else:
            regCarro = Carro(producto=regProducto, usuario= regUsuario, valUnit = regProducto.precioUnitario)
        
        # guardar el registro
        regCarro.save()

     
        # dar mensaje
        #msj = 'Producto no disponible'

        # redireccionar a 'verProducto'
    return verCategorias(request) 



def verCarrito(request):
    context = consultarCarro(request)
    return render(request, 'productos/carrito.html', context)



"""
    Función auxiliar
"""
def consultarCarro(request):
    #get usuario
    regUsuario = request.user
    #filtrar productos de ese usuario en estado 'activo'
    listaCarrito = Carro.objects.filter(usuario= regUsuario, estado= 'activo').values('id', 'cantidad', 'valUnit', 'producto__imgPeque', 'producto__nombre','producto__unidad', 'producto__id')
    #renderizar
    listado = []
    subtotal = 0
    for prod in listaCarrito:
        reg = {
            'id': prod['id'],
            'cantidad':  prod['cantidad'],
            'valUnit':  prod['valUnit'],
            'imgPeque':  prod['producto__imgPeque'],
            'nombre':  prod['producto__nombre'],
            'unidad':   prod['producto__unidad'],
            'total':   prod['valUnit'] * prod['cantidad'],
            'prodId':   prod['producto__id'],
        }
        subtotal += prod['valUnit'] * prod['cantidad']

        listado.append(reg)
    
    envio = 8000
    if len(listado) == 0:
        envio = 0

    context = {
        'titulo': 'Productos en el carrito de compras',
        'carrito': listado,
        'subtotal': subtotal,
        'iva': int(subtotal) * 0.19,
        'envio': envio,
        'total': int(subtotal) * 1.19 + envio
    }

    return context
