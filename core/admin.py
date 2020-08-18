from django.contrib import admin

from .models.product import Product
from .models.category import Category
from .models.store import Store
from .models.user import User

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(User)
