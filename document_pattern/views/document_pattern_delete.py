from .imports import *


@login_required
def document_pattern_delete(request, doc_id):
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    DocumentPattern.objects.get(id=doc_id).delete()
    return redirect(reverse('document_pattern:list'))
