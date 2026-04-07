"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home-systems/', views.category_page, {"category": "residential"}, name='residential'),
    path('site-systems/', views.category_page, {"category": "commercial"}, name='commercial'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<slug:slug>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders_view, name='orders'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
