from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','pub_date']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['categoria','nombre','precio','stock','pub_date']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)