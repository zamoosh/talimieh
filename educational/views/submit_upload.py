from .imports import *


def submit_upload(request, r_id=None):
    if request.method == 'POST':
        if request.FILES:
            o = OwnerDocument.objects.create(
                user=request.user,
                title=request.POST.get('title'),
                image=request.FILES.get('file')
            )
            o.save()
            if r_id:
                r = EducationalRequest.objects.get(id=r_id)
                r.ownerdocument_set.add(o)
                r.save()
                return redirect(reverse('educational:request_single_detail', args=[r_id]))
    return redirect(reverse('educational:uni_request_submit'))
