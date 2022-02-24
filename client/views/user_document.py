from .imports import *
from ..models import Owner_document


def user_document(request):
    context = {}
    context['documents'] = Owner_document.objects.filter(owner=request.user.id)
    return render(request, 'client/user_document.html', context)

def user_document_upload(request):
    context = {}
    if request.method == "POST":
        context['title'] = request.POST.get('title', '').strip()
        document = Owner_document()
        if 'owner_upload' in request.FILES:
            document.image = request.FILES['owner_upload']
        document.owner_id = request.user.id
        document.title = context['title']
        document.save()
        context['result'] = True
    return render(request, 'client/user_document_upload.html', context)
