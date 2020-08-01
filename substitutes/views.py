from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .forms import SubstituteSearchForm
from django.views import View

from django.views.generic import ListView

from .utils import find_substitute

from core.models.product import Product

class SubstituteView(View):

    search_substitute_form = SubstituteSearchForm
    template_name = 'substitutes/substitute.html'
    context = {} 

    def get(self, request):     
              
       
        product_name = request.GET.get('product')        
        product, substitute_list = find_substitute(product_name)
        num_substitutes = len(substitute_list)

        page = request.GET.get('page', 1)   
        paginator = Paginator(substitute_list, 6)       
                
        try:
            substitute_pages = paginator.page(page)
        except PageNotAnInteger:
            substitute_pages = paginator.page(1)
        except EmptyPage:
            substitute_pages = paginator.page(paginator.num_pages)
        
        self.context['product'] = product
        self.context['num_substitutes'] = num_substitutes   
        
        self.context['substitute_list'] = substitute_list
        self.context["substitute_pages"] = substitute_pages 
                       
        return render(request, self.template_name, self.context)



# class SubstituteListView(ListView):
#     model = Product
#     template_name = 'substitutes/substitute.html'
#     paginate_by = 6
#     context = {}


#     def get_queryset(self):

#         product_name = self.request.GET.get('product') 
#         product, substitute_list = find_substitute(product_name)
#         num_substitutes = len(substitute_list)

#         self.context['product'] = product
#         self.context['num_substitutes'] = num_substitutes   
        
#         self.context['substitute_list'] = substitute_list

#         return product, substitute_list


#     def get_context_data(self, **kwargs):
#         context = super(SubstituteListView, self).get_context_data(**kwargs)
#         context['form'] = SubstituteSearchForm()

#         return context


