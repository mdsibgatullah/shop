# from django.urls import path
# from limupapp.views import AboutUs, BlogDetailsLeftSidebar, Error, Index, ShopLeftSidebar

from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('error/',views.Error.as_view(), name='error'),
    path('about-us/',views.AboutUs.as_view(), name='about-us'),
    path('shop/',views.ShopLeftSidebar.as_view(), name='shop'),
    path('single-product/<slug>',views.SingleProduct.as_view(), name='single-product'), #off link
    path('blog-details-left-sidebar/',views.BlogDetailsLeftSidebar.as_view(), name='blog-details-left-sidebar'),
    path('blog-left-sidebar/',views.BlogLeftSidebar.as_view(), name='blog-left-sidebar'),
    path('checkout/',views.Checkout.as_view(), name='checkout'),
    path('compare/',views.Compare.as_view(), name='compare'),
    path('contact/',views.Contact.as_view(), name='contact'),
    path('faq/',views.Faq.as_view(), name='faq'),
    path('login/',views.loginRegister.as_view(), name='login'),
    path('wishlist/',views.Wishlist.as_view(), name='wishlist'),
]
