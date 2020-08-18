from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.views import generic

from core.models.managers.product_manager import ProductManager
from core.models.product import Product


class FavouriteView(LoginRequiredMixin, generic.ListView):

    """This class displays and manages the favourites view.

    """
    model = Product
    paginate_by = 6
    context_object_name = 'favourites'

    template_name = 'favourites/favourites.html'
    login_url = '/login/'

    def get_queryset(self):
        current_user = self.request.user

        return current_user.product_set.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_favourites'] = self.request.user.product_set.all().count()

        return context

    def post(self, request):

        current_user = request.user

        if request.method == 'POST':

            if request.POST['action'] == 'Sauvegarder':

                # product_barcode = request.POST.get('product_barcode')
                product_name = request.POST.get('product_name')
                substitute_barcode = request.POST.get('substitute_barcode')
                substitute = ProductManager().get_product_by_barcode(
                    substitute_barcode)

                current_user.product_set.add(substitute)
                messages.info(request, "Le produit a été ajouté à vos favoris")

                return redirect(f"/substitute/?product={product_name}")

            elif request.POST['action'] == 'Supprimer':

                substitute_barcode = request.POST.get('substitute_barcode')
                substitute = ProductManager().get_product_by_barcode(
                    substitute_barcode)

                current_user.product_set.remove(substitute)
                messages.info(request, "Le produit a été retiré à vos favoris")

                return redirect("/favourites/")

            return redirect("/")
