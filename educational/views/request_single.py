from .imports import *


def request_single(request, r_id=None):
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if r.status:
                r.status = False
                r.request_expert = None
                r.user.expert = None
                r.step = EducationalRequest.REQUEST_STEPS[0]
            else:
                r.status = True
                r.request_expert = request.user
                r.user.expert = request.user
                m = Message.objects.create(
                    text=f'درخواست شما مبنی بر {r.title} تائید شد',
                    educational_request=r,
                    owner=r.user,
                    message_expert=request.user,
                )
                m.save()
            r.step = EducationalRequest.REQUEST_STEPS[1]
            r.save()
        return redirect(reverse('educational:requests'))
    r = EducationalRequest.objects.get(id=request.GET.get('r'))
    context = {}
    context['r'] = r
    context['selected_semesters'] = r.selectedsemester_set.all()
    context['user'] = r.user
    return render(request, 'educational/request_single.html', context)
