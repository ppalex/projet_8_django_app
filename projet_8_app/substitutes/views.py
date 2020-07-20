from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SubstituteSearchForm
from django.views import View

class SubstituteView(View):

    search_substitute_form = SubstituteSearchForm
    template_name = 'substitutes/substitute.html'

    def post(self, request):
        form = self.search_substitute_form(request.POST)
        context = {'form' : form}

        if form.is_valid():
         
            product = form.cleaned_data['text']
            
                                
            return render(request, self.template_name, context)