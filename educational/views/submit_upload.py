from .imports import *


def submit_upload(request):
    if request.method == 'POST':
        if request.FILES:
            o = OwnerDocument.objects.create(
                user=request.user,
                title=request.POST.get('title'),
                image=request.FILES.get('file')
            )
            o.save()
    return redirect(reverse('educational:uni_request_submit'))
