# api/admin.py
from django.contrib import admin
from api.models import Stock_En_Tienda, Tienda, Categoria,Producto,SubCategoria

admin.site.register(Stock_En_Tienda)
admin.site.register(Tienda)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto)