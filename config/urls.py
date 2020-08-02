"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path

from core.views import index
from users.views import RegisterView, ProfileView, CustomLoginView, CustomLogoutView

from substitutes.views import SubstituteView
from products.views import ProductView
from favourites.views import FavouriteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    re_path(r'^substitute/$', SubstituteView.as_view(), name='substitute'),
    path('product/<int:barcode>/', ProductView.as_view(), name='product'),
    path('favourites/', FavouriteView.as_view(), name='favourite')
    
]
