from django.contrib import admin

from compraventa.models import cliente, compra, deposito, producto, proveedor, venta
from compraventa.models import  *

# Register your models here.

admin.site.register(proveedor)
admin.site.register(deposito)
admin.site.register(producto)
admin.site.register(compra)
admin.site.register(venta)
admin.site.register(cliente)