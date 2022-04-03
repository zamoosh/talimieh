from .imports import *


def request_single(request, r_id=None):
    if request.method == 'GET':
        r = EducationalRequest.objects.get(id=request.GET.get('r'))
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if r.status:
                r.status = False
            else:
                r.status = True
            r.save()
            return redirect(reverse('educational:requests'))
    return HttpResponse('salam')
