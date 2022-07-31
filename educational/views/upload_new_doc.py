from .imports import *


def upload_new_doc(request):
    response = is_id_real(DocumentPattern, request.GET.get('document_pattern'))
    if response:
        return response
    if not request.GET.get('document_pattern'):
        request.session['select'] = True
        return redirect(reverse('client:user_document'))
    context = {}
    if request.GET.get('r_id'):
        context['to_request'] = True
        context['r_id'] = request.GET.get('r_id')
    context['document_pattern'] = DocumentPattern.objects.get(id=request.GET.get('document_pattern'))
    context['types'] = context['document_pattern'].types['types']
    return render(request, 'educational/upload_new_doc.html', context)
