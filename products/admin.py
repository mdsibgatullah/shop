from django.contrib import admin

from products.models import GalleryImgs, Product

# Register your models here.
admin.site.register(GalleryImgs)
admin.site.register(Product)