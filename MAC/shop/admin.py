from django.contrib import admin
from . models import Product,Contact,Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)