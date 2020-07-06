def settings(request):
    """
    Put selected settings variables into the default template context
    """
    from django.conf import settings
    return {
        'API_OFF': settings.API_OFF
    }