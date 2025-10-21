from django.shortcuts import render
from .models import Product

"""
El archivo views.py en Django es donde defines las vistas de tu aplicación
web. Las vistas son funciones o clases que reciben solicitudes HTTP y devuelven
respuestas."""
# Create your views here.

# Vista para la página de inicio
from django.shortcuts import render
from .models import Product, Category

def home(request):
    query = request.GET.get('name')
    category_id = request.GET.get('category')

    products = Product.objects.all()
    
    if category_id and category_id != "todo":
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()  # ahora las categorías vienen de la DB

    return render(request, 'xocolatl_catalogo/index.html', {
        'products': products,
        'categories': categories,
    })



from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Product

def filter_products(request):
    category_id = request.GET.get("category")
    name_query = request.GET.get("name")

    products = Product.objects.all()

    if category_id and category_id != "todo":
        products = products.filter(category_id=category_id)
    
    if name_query:
        products = products.filter(name__icontains=name_query)

    html = render_to_string("partials/products_list.html", {"products": products}, request=request)
    return JsonResponse({"html": html})

