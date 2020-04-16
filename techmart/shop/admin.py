from django.contrib import admin
from .models import product, banner, order_update, order

admin.site.register(product)
admin.site.register(banner)
admin.site.register(order_update)
admin.site.register(order)

