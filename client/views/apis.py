from django.http import JsonResponse
from .imports import *
from client.models import *
from django.db.models import Q


@login_required
def get_document(request):
    # context = []
    # q = Q(owner=request.user)
    # for i in OwnerDocument.objects.filter(q & ~Q(image=None)):
    #     if i.image:
    #         context.append({'id': i.pk, 'title': i.title, 'image': i.image.url})
    # return JsonResponse(context, safe=False)
    context = []
    for i in OwnerDocument.objects.filter(image__isnull=False):
        context.append({'id': i.pk, 'title': i.title, 'image': i.image.url})
    return JsonResponse(context, safe=False)
