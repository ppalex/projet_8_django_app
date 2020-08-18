from django.shortcuts import render


from substitutes.forms import SubstituteSearchForm


def index(request):
    """This function displays the home page views.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response for the home page view.
    """

    form = SubstituteSearchForm()
    context = {'form': form}

    return render(request, 'core/home.html', context)


def legal_notice(request):
    """This function displays the home page views.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response view for the legal notice view.
    """
    return render(request, 'core/legal_notice.html')
