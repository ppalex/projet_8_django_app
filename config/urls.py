
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path

from core.views import index, legal_notice
from users.views import RegisterView, ProfileView, CustomLoginView, CustomLogoutView

from substitutes.views import SubstituteView
from products.views import ProductView
from favourites.views import FavouriteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('legal_notice/', legal_notice, name="legal_notice"),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    re_path('^substitute/$', SubstituteView.as_view(), name='substitute'),
    path(r'product/<int:barcode>/', ProductView.as_view(), name='product'),
    path('favourites/', FavouriteView.as_view(), name='favourite')
    
]
