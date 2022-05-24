from django.http import JsonResponse
from .imports import *


@login_required
def get_document(request):
    context = []
    for i in OwnerDocument.objects.filter(image__isnull=False, user=request.user):
        context.append({'id': i.pk, 'title': i.title, 'image': i.image.url})
    return JsonResponse(context, safe=False)
