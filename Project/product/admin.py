from django.contrib import admin

from .models import Product,ProductImage,category ,Product_Alterative ,Product_Accessories
 

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(category)
admin.site.register(Product_Alterative)
admin.site.register(Product_Accessories)