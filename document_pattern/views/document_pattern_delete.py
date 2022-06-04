from .imports import *


@login_required
def document_pattern_delete(request, doc_id):
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    d = DocumentPattern.objects.get(id=doc_id)
    docs = d.ownerdocument_set.all()
    for owner_doc in docs:
        owner_doc.extra['pattern_confirm'] = False
    d.status = False
    d.save()
    return redirect(reverse('document_pattern:list'))
