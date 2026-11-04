from django.http import HttpResponse, Http404

# ჩვენი "ბაზა"
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1800},
    {"id": 2, "name": "Headphones", "price": 150},
    {"id": 3, "name": "Mouse", "price": 40},
]


def home(request):
    html = "<h1>myshop</h1><a href='/products/'>produqtis naxva</a>"
    return HttpResponse(html)


def about(request):
    return HttpResponse(
        "ეს არის ჩვენი პირველი Django ონლაინ მაღაზია. აქ ვსწავლობთ Django-ს መሰვლებს და URL-ების მართვას.")


def product_list(request):
    items_html = "".join([
        f"<li><a href='/products/{p['id']}/'>{p['name']}</a>: {p['price']} ₾</li>"
        for p in PRODUCTS
    ])
    return HttpResponse(f"<ul>{items_html}</ul>")


def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)

    if product is None:
        raise Http404("produqti ver moidzewbna")

    return HttpResponse(f"{product['name']}: {product['price']} ₾")