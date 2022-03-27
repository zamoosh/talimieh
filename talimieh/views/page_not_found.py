from .imports import *


def page_not_found(request):
    return render(request, '404_page.html')
