from django.shortcuts import get_object_or_404,render
from .models import Producto,Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')#[:6]
    cat_list = Categoria.objects.order_by('nombre')
    context = {'product_list':product_list,
               'cat_list':cat_list}
    return render (request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    cat_list = Categoria.objects.order_by('nombre')
    context = {'producto':producto,
               'cat_list':cat_list}
    return render(request, 'producto.html', context)

def categoria(request, categoria_id):
    cat = get_object_or_404(Categoria, pk = categoria_id)
    cat_list = Categoria.objects.order_by('nombre')
    product_list = Producto.objects.filter(categoria = cat.id)
    context = {'product_list':product_list,
               'cat_list':cat_list,
               'categoria_id':categoria_id}
    return render(request, 'categoria.html', context)