"""
URL configuration for dripshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include(('dripshop_apps.core.urls', 'core'), namespace='core')),
    path('product/', include(('dripshop_apps.product.urls', 'product'), namespace='product')),
    path('category/', include(('dripshop_apps.category.urls', 'category'), namespace='category')),
    path('brand/', include(('dripshop_apps.brand.urls', 'brand'), namespace='brand')),
    path('cart', include(('dripshop_apps.cart.urls', 'cart'), namespace='cart')),
    path('order/', include(('dripshop_apps.order.urls', 'order'), namespace='order')),
    path('wishlist/', include(('dripshop_apps.wishlist.urls', 'wishlist'), namespace='wishlist')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)