from .imports import *


@login_required
def user_document(request):
    context = {}
    context['documents'] = OwnerDocument.objects.filter(user=request.user.id)
    context['document_pattern'] = DocumentPattern.objects.filter(status=True)
    if request.session.get('select'):
        context['select'] = True
        del request.session['select']
    return render(request, 'client/user_document.html', context)
