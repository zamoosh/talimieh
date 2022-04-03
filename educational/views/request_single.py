from .imports import *


def request_single(request, r_id=None):
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            if request.user.user_permissions.filter(name__contains='register'):
                if r.register_status is False:
                    r.register_status = True
                    r.request_expert_register = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} توسط {request.user} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[1]
                    m.save()
            elif request.user.user_permissions.filter(name__contains='financial'):
                if r.financial_status is False:
                    r.financial_status = True
                    r.request_expert_financial = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} توسط {request.user} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[2]
                    m.save()
            elif request.user.user_permissions.filter(name__contains='educational'):
                if r.educational_status is False:
                    r.educational_status = True
                    r.request_expert_educational = request.user
                    r.user.expert = request.user
                    m = Message.objects.create(
                        text=f'درخواست شما مبنی بر {r.title} توسط {request.user} تائید شد',
                        educational_request=r,
                        owner=r.user,
                        message_expert=request.user,
                    )
                    r.step = EducationalRequest.REQUEST_STEPS[3]
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


def request_single_remove(request, r_id):
    if not request.user.user_permissions.filter(name__contains='see'):
        return redirect('/')
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            Message.objects.create(
                text=f'درخواست شما مبنی بر {r.title} توسط {request.user} رد شد',
                educational_request=None,
                owner=r.user,
                message_expert=request.user,
            ).save()
            if request.user.user_permissions.filter(name__contains='register'):
                r.delete()
            elif request.user.user_permissions.filter(name__contains='financial'):
                r.delete()
            elif request.user.user_permissions.filter(name__contains='educational'):
                r.delete()
    return redirect(reverse('educational:requests'))
