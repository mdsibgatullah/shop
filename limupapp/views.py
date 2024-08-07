from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView

from limupapp.models import Category, Slider
from products.models import Product

# Create your views here.

# ------------------------- index ______
class Index(TemplateView):
    template_name = 'limupapp/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['home_slider'] = Slider.objects.filter(name='Main Sliders')
        context['products'] = Product.objects.all()

        return context

# ------------------------- 404 ______
class Error(TemplateView):
    template_name = 'limupapp/404.html'

# ------------------------- about-us ______
class AboutUs(TemplateView):
    template_name = 'limupapp/about-us.html'

# ------------------------- blog-details-left-sidebar ______
class BlogDetailsLeftSidebar(TemplateView):
    template_name = 'limupapp/blog-details-left-sidebar.html'

# ------------------------- blog-left-sidebar ______
class BlogLeftSidebar(TemplateView):
    template_name = 'limupapp/blog-left-sidebar.html'

# ------------------------- cart ______
class Cart(TemplateView):
    template_name = 'limupapp/cart.html'

# ------------------------- checkout ______
class Checkout(TemplateView):
    template_name = 'limupapp/checkout.html'

# ------------------------- compare ______
class Compare(TemplateView):
    template_name = 'limupapp/compare.html'

# ------------------------- contact ______
class Contact(TemplateView):
    template_name = 'limupapp/contact.html'

# ------------------------- faq ______
class Faq(TemplateView):
    template_name = 'limupapp/faq.html'

# ------------------------- login-register ______
class loginRegister(TemplateView):
    template_name = 'limupapp/login-register.html'

# ------------------------- shop-left-sidebar ______
class ShopLeftSidebar(TemplateView):
    template_name = 'limupapp/shop-left-sidebar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

# ------------------------- single-product ______
class SingleProduct(TemplateView):
    template_name = 'limupapp/single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['product'] = Product.objects.get(slug=slug)
        return context

# ------------------------- Wishlist ______
class Wishlist(TemplateView):
    template_name = 'limupapp/wishlist.html'