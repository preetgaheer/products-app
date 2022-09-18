from django.contrib import admin

# Register your models here.
from .models import ProductApi, ProductDetails
  
# Register your models here.  
admin.site.register(ProductApi)  
admin.site.register(ProductDetails)