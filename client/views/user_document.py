from .imports import *


@login_required
def user_document(request):
    context = {}
    context['documents'] = OwnerDocument.objects.filter(user=request.user.id)
    context['amount_of_doc'] = request.user.ownerdocument_set.all().__len__()
    context['document_pattern'] = DocumentPattern.objects.filter(status=True)
    return render(request, 'client/user_document.html', context)
