from django.urls import path
from .views import ver_stock, pagina_principal

urlpatterns = [
    path('', pagina_principal),      # sirve el HTML en la raíz
    path('stock/', ver_stock),       # API para ver stock
]
