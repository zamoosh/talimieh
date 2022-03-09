from .imports import *


def upload_new_doc(request):
    return render(request, 'educational/upload_new_doc.html')
