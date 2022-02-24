from django.http import JsonResponse
from .imports import *
from client.models import *

@login_required
def get_document(request):
    context = []
    for i in Owner_document.objects.filter(owner=request.user.id):
        context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)
