from .imports import *


def user_document(request):
    context = {'documents': OwnerDocument.objects.filter(user=request.user.id)}
    return render(request, 'client/user_document.html', context)


def user_document_upload(request):
    context = {}
    if request.method == "POST":
        context['title'] = request.POST.get('title', '').strip()
        document = OwnerDocument()
        if 'owner_upload' in request.FILES:
            document.image = request.FILES['owner_upload']
        document.user = request.user
        document.title = context['title']
        document.save()
        context['result'] = True
        context['document'] = document
        return HttpResponseRedirect(reverse('educational:uni_request_submit'))
    return render(request, 'client/user_document_upload.html', context)
