from .imports import *


def request_single(request, r_id=None):
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if r.status:
                r.status = False
                r.request_expert = None
            else:
                r.status = True
                r.request_expert = request.user
            r.save()
        return redirect(reverse('educational:requests'))
    r = EducationalRequest.objects.get(id=request.GET.get('r'))
    context = {}
    context['r'] = r
    context['selected_semesters'] = r.selectedsemester_set.all()
    context['user'] = r.user
    return render(request, 'educational/request_single.html', context)
