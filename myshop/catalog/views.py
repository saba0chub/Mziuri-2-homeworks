from django.http import HttpResponse, Http404
from django.urls import reverse

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1800},
    {"id": 2, "name": "Headphones", "price": 150},
    {"id": 3, "name": "Mouse", "price": 40},
]

def home(request):
    products_url = reverse('product_list')
    html = f"<h1>myshop (Ubuntu)</h1><p><a href='{products_url}'>Productebi</a></p>"
    return HttpResponse(html)

def about(request):
    return HttpResponse("myshop ragac")

def product_list(request):
    items_html = "".join([
        f"<li><a href='/products/{p['id']}/'>{p['name']}</a>: {p['price']} ₾</li>"
        for p in PRODUCTS
    ])
    return HttpResponse(f"<ul>{items_html}</ul>")

def product_detail(request, pk):
    product = next((p for p in PRODUCTS if p['id'] == pk), None)
    if not product:
        raise Http404("produqti ar moidzebna")
    return HttpResponse(f"{product['name']}: {product['price']} ₾")