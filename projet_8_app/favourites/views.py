from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from django.core.paginator import Paginator

from core.models.managers.product_manager import ProductManager

from django.contrib import messages

class FavouriteView(View):

    template_name = 'favourites/favourites.html'

    def get(self, request):     
        
        current_user = request.user

        favourites = current_user.product_set.all()

        context = {'favourites': favourites}

        return render(request, self.template_name, context)
    
    def post(self, request):
        
        context = {}

        current_user = request.user
        product_barcode = request.POST.get('product_barcode')
        product_name = request.POST.get('product_name')
        substitute_barcode = request.POST.get('substitute_barcode')        

        if request.method == 'POST':
            if request.POST['favourite_save'] == 'Sauvegarder':
               
                product = ProductManager().get_product_by_barcode(product_barcode)
                substitute = ProductManager().get_product_by_barcode(substitute_barcode)
                
                current_user.product_set.add(substitute)
                messages.info(request, "Le produit a été ajouté à vos favoris")
        
        return redirect(f"/substitute/?product={product_name}")