from django.shortcuts import render
from django.http import JsonResponse


from substitutes.forms import SubstituteSearchForm
from core.models.product import Product


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


def autocomplete(request):
    """This function displays the home page views.

    Args:
        request ([HttpRequest]): Contains the metadata about the request.

    Returns:
        [ HttpResponse]: Contains the response for the home page view.
    """

    if 'term' in request.GET:

        print(request.GET.get('term'))

        query = Product.product_objects.filter(
            product_name__istartswith=request.GET.get('term'))

        product_names = list()

        for product in query:
            product_names.append(product.product_name)

        return JsonResponse(product_names, safe=False)

    form = SubstituteSearchForm()
    context = {'form': form}

    return render(request, 'core/home.html', context)
