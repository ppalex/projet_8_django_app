from django.http import HttpResponseRedirect
from django.shortcuts import render


from .forms import SubstituteSearchForm
from django.views import View

from .utils import find_substitute

class SubstituteView(View):

    search_substitute_form = SubstituteSearchForm
    template_name = 'substitutes/substitute.html'


    def get(self, request):
       
        context = {}        
    
        product_name = request.GET.get('product')
        
        product, substitute_list = find_substitute(product_name)

        context['product'] = product
        context['substitute_list'] = substitute_list
                            
        return render(request, self.template_name, context)

   
    # def post(self, request):
    #     form = self.search_substitute_form(request.POST)
    #     context = {'form' : form}

    #     if form.is_valid():
         
    #         product_name = form.cleaned_data['text']
            
    #         product, substitute_list = find_substitute(product_name)

    #         context['product'] = product
    #         context['substitute_list'] = substitute_list
                                
    #         return render(request, self.template_name, context)
