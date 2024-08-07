from django.contrib import admin

from limupapp.models import Category, Slider, SliderItem, SubCategory, SubSubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubSubCategory)
admin.site.register(SubCategory)
admin.site.register(SliderItem)
admin.site.register(Slider)