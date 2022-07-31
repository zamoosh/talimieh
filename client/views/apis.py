from django.http import JsonResponse
from .imports import *


@login_required
def get_document(request):
    context = []
    for i in OwnerDocument.objects.filter(file__isnull=False, user=request.user):
        context.append({'id': i.pk, 'title': i.title, 'file': i.file.url})
    return JsonResponse(context, safe=False)
