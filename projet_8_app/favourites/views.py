from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from django.core.paginator import Paginator

from core.models.managers.product_manager import ProductManager

class FavouriteView(View):



    def get(self, request):
        pass

    
    def post(self, request):
        template_name = 'substitutes/substitute.html'
        context = {}

        product_barcode = request.POST.get('product_barcode')
        product_name = request.POST.get('product_name')
        substitute_barcode = request.POST.get('substitute_barcode')        

        if request.method == 'POST':
            if request.POST['favourite_save'] == 'Sauvegarder':
               
                product = ProductManager().get_product_by_barcode(product_barcode)
                substitute = ProductManager().get_product_by_barcode(substitute_barcode)
                product.substitutes.add(substitute)
        
        return redirect(f"/substitute/?product={product_name}") 