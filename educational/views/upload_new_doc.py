from .imports import *


def upload_new_doc(request):
    context = {}
    if request.GET.get('r_id'):
        context['to_request'] = True
        context['r_id'] = request.GET.get('r_id')
    if int(request.GET.get('document_pattern')):
        context['document_pattern'] = DocumentPattern.objects.get(id=request.GET.get('document_pattern'))
    return render(request, 'educational/upload_new_doc.html', context)
