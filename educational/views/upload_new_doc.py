from .imports import *


def upload_new_doc(request):
    if not request.GET.get('document_pattern'):
        request.session['select'] = True
        return redirect(reverse('client:user_document'))
    context = {}
    if request.GET.get('r_id'):
        context['to_request'] = True
        context['r_id'] = request.GET.get('r_id')
    context['document_pattern'] = DocumentPattern.objects.get(id=request.GET.get('document_pattern'))
    return render(request, 'educational/upload_new_doc.html', context)
