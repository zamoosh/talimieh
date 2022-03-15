from .imports import *


def request_single(request, r_id=None):
    if request.method == 'GET':
        r = EducationalRequest.objects.get(id=request.GET.get('r'))
        context = {}
        context['request'] = r
        context['selected_semesters'] = r.selectedsemester_set.all()
        context['user'] = r.user
        return render(request, 'educational/request_single.html', context)
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if r.status:
                r.status = False
            else:
                r.status = True
            r.save()
        return redirect(reverse('educational:requests'))
