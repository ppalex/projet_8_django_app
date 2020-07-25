from django.shortcuts import render
from django.views import View

from core.models.managers.product_manager import ProductManager

class ProductView(View):
    
    template_name = 'products/product_detail.html'


    def post(self, request, barcode):
        product = ProductManager().get_product_by_barcode(barcode)
        context = {'product' : product}

        return render(request, self.template_name, context)