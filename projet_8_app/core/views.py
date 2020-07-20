from django.shortcuts import render


from substitutes.forms import SubstituteSearchForm

def index(request):

    form = SubstituteSearchForm()

    context = {'form' : form}

    return render(request, 'core/home.html', context)