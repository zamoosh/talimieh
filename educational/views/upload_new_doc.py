from .imports import *


def upload_new_doc(request):
    context = {}
    if request.GET.get('r_id'):
        context['to_request'] = True
        context['r_id'] = request.GET.get('r_id')
    return render(request, 'educational/upload_new_doc.html', context)
