# from django.urls import path
# from limupapp.views import AboutUs, BlogDetailsLeftSidebar, Error, Index, ShopLeftSidebar

# urlpatterns = [
#     path('',Index.as_view(), name='index'),
#     path('error/',Error.as_view(), name='error'),
#     path('about-us/',AboutUs.as_view(), name='about-us'),
#     path('shop-left-sidebar/',ShopLeftSidebar.as_view(), name='shop-left-sidebar'),
#     path('blog-details-left-sidebar/',BlogDetailsLeftSidebar.as_view(), name='blog-details-left-sidebar'),
# ]

from django.urls import path
from limupapp.views import AboutUs, BlogDetailsLeftSidebar, Error, Index, ShopLeftSidebar, SingleProduct

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('error/',Error.as_view(), name='error'),
    path('about-us/',AboutUs.as_view(), name='about-us'),
    path('shop/',ShopLeftSidebar.as_view(), name='shop'),
    path('single-product/<slug>',SingleProduct.as_view(), name='single-product'),
    path('blog-details-left-sidebar/',BlogDetailsLeftSidebar.as_view(), name='blog-details-left-sidebar'),
]
