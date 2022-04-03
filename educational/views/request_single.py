from .imports import *


def request_single(request, r_id=None):
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if request.user.groups.filter(name__contains='ثبت‌نام'):
                if r.register_status:
                    r.register_status = False
                    r.request_expert_register = None
                    r.user.expert = None
                    r.step = EducationalRequest.REQUEST_STEPS[0]
                else:
                    r.register_status = True
                    r.request_expert_register = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[1]
                    m.save()
            elif request.user.groups.filter(name__contains='مالی'):
                if r.financial_status:
                    r.financial_status = False
                    r.request_expert_financial = None
                    r.user.expert = None
                    r.step = EducationalRequest.REQUEST_STEPS[0]
                else:
                    r.financial_status = True
                    r.request_expert_financial = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[1]
                    m.save()
            elif request.user.groups.filter(name__contains='آموزشی'):
                if r.educational_status:
                    r.educational_status = False
                    r.request_expert_educational = None
                    r.user.expert = None
                    r.step = EducationalRequest.REQUEST_STEPS[0]
                else:
                    r.educational_status = True
                    r.request_expert_educational = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[1]
                    m.save()
            r.save()
        return redirect(reverse('educational:requests'))
    if request.GET.get('r'):
        r = EducationalRequest.objects.get(id=request.GET.get('r'))
        context = {}
        context['r'] = r
        context['selected_semesters'] = r.selectedsemester_set.all()
        context['user'] = r.user
        return render(request, 'educational/request_single.html', context)
    return redirect(reverse('educational:requests'))
