from substitutes.forms import SubstituteSearchForm


def core(request):
    """This function creates a context processor with data needed.

    Args:
        request ([type]): [description]

    Returns:
        [kwargs]: Contains all data stored in the context processor.
    """
    kwargs = {
        'search_bar_form': SubstituteSearchForm,
    }
    return kwargs
