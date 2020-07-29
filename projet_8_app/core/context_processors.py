from django.conf import settings

from substitutes.forms import SubstituteSearchForm

def core(request):
    kwargs = {
        'search_bar_form': SubstituteSearchForm,
        
    }
    return kwargs