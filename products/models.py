from django.db import models
from django.utils.text import slugify

# Create your models here.
from django.db import models

from limupapp.models import Category, SubCategory, SubSubCategory

class GalleryImgs(models.Model):
    pd_imgs = models.ImageField()

class Product(models.Model):
    # Define choices for product type
    TYPE_CHOICES = [
        ('FEATURED', 'FEATURED'),
        ('RAGULAR', 'RAGULAR'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    # discount_percentage = models.IntegerField(blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_hot_deal = models.BooleanField(default=False)
    hot_deal_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    stock_quantity = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    gallery_images = models.ManyToManyField(GalleryImgs)

    def save(self, *args, **kwargs):
        if not self.discount_percentage:#50-30=10*100/50(regularPrice-offerPrice*100/regularPrice)
            self.discount_percentage = (self.regular_price-self.offer_price)*100/self.regular_price
        if not self.slug:
            self.slug = slugify(self.name[:20])
        super(Product, self).save()

    def __str__(self):
        return self.name
