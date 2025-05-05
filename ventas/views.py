import os
from django.http import JsonResponse, HttpResponse

def ver_stock(request):
    stock = {
        "sucursal1": {"cantidad": 31, "precio": 333},
        "sucursal2": {"cantidad": 23, "precio": 222},
        "sucursal3": {"cantidad": 100, "precio": 1111},
        "casa_matriz": {"cantidad": 10, "precio": 999}
    }
    return JsonResponse(stock)

def pagina_principal(request):
    ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'index.html')
    with open(ruta, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())
