from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class SubSubCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name[:20])
        super(SubSubCategory, self).save()

class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    sub_sub_category = models.ManyToManyField(SubSubCategory, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name[:20])
        super(SubCategory, self).save()

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    sub_category = models.ManyToManyField(SubCategory, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name[:20])
        super(Category, self).save()

class SliderItem(models.Model):
    name = models.CharField(max_length=20)
    text = RichTextField()
    btn_text = models.CharField(max_length=50)
    btm_url = models.ImageField()
    def __str__(self):
        return self.name
    
class Slider(models.Model):
    name = models.CharField(max_length=50)
    slider_item = models.ManyToManyField(SliderItem)
    def __str__(self):
        return self.name



