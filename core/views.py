from django.shortcuts import render


from substitutes.forms import SubstituteSearchForm

def index(request):

    form = SubstituteSearchForm()

    context = {'form' : form}

    return render(request, 'core/home.html', context)


def legal_notice(request):
    return render(request, 'core/legal_notice.html')