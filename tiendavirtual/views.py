from django.shortcuts import render
from .models import Categorias, Clientes, Companiasdeenvios, Pedidos, Proveedores, Productos, Detallesdepedidos 

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_clientes=Clientes.objects.all().count()
    num_proveedores=Proveedores.objects.all().count()
    num_productos=Productos.objects.filter(demanda__exact='m').count()
    num_mensajeros=Companiasdeenvios.objects.count()
    Prod2=Productos.objects.get(pk=2)
    imProd2=Prod2.imagentest.url
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_clientes':num_clientes,'num_proveedores':num_proveedores,'num_productos':num_productos,'num_mensajeros':num_mensajeros},#,'imProd1':imProd1},
    )

from django.views import generic

class ProductListView(generic.ListView):
    model = Productos

class ProductDetailView(generic.DetailView):
    model = Productos

#comentario de prueba
"""def product_detail_view(request,pk):
    try:
        prod_id=Productos.objects.get(pk=pk)
    except Productos.DoesNotExist:
        raise Http404("Productos does not exist")
    
    return render(
        request,
        'tiendavirtual/productos_detail.html',
        context={'producto':prod_id,}
    )"""