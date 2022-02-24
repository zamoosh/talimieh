from .imports import *


def document(request):
    context = {}

    return render(request, '', context)
