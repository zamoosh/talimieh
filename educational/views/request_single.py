from .imports import *


def conditions_for_requests(request: 'django request', r, context):
    context['r_con'] = False
    context['e_con'] = False
    context['f_con'] = False
    context['e_con_2'] = False
    context['f_con_2'] = False
    if r.reject is False and (request.user.is_superuser or request.user.user_permissions.filter(name__contains='see')):
        if int(r.step[1]) == 1:
            context['r_con'] = True
        elif int(r.step[1]) == 2:
            context['e_con'] = True
        elif int(r.step[1]) == 3:
            context['f_con'] = True
        elif int(r.step[1]) == 4:
            context['e_con_2'] = True
        elif int(r.step[1]) == 5:
            context['f_con_2'] = True
        elif int(r.step[1]) == 6:
            context['e_con_3'] = True


@login_required
def request_single(request, r_id=None):
    if request.GET.get('r'):
        r = EducationalRequest.objects.get(id=request.GET.get('r'))
        context = {}
        context['r'] = r
        context['selected_semesters'] = r.selectedsemester_set.all()
        context['user'] = r.user
        context['documents'] = r.ownerdocument_set.all()
        context['amount_of_doc'] = r.ownerdocument_set.all().__len__()
        conditions_for_requests(request, r, context)
        return render(request, 'educational/request_single.html', context)
    if request.method == 'POST' and r_id:
        if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
            return redirect(reverse('page_not_found'))
        r = EducationalRequest.objects.get(id=r_id)
        if r.reject is False:
            m = Message.objects.create(
                text=f'درخواست شما مبنی بر {r.title} توسط {request.user} تائید شد',
                educational_request=r,
                owner=r.user,
                message_expert=request.user,
            )
            if int(r.step[1]) == 1:
                r.request_expert_register = request.user
                r.step = EducationalRequest.REQUEST_STEPS[1]
            elif int(r.step[1]) == 2:
                r.request_expert_educational = request.user
                r.step = EducationalRequest.REQUEST_STEPS[2]
            elif int(r.step[1]) == 3:
                r.request_expert_financial = request.user
                r.step = EducationalRequest.REQUEST_STEPS[3]
            elif int(r.step[1]) == 4:
                r.request_expert_educational = request.user
                r.step = EducationalRequest.REQUEST_STEPS[4]
            elif int(r.step[1]) == 5:
                r.request_expert_financial = request.user
                r.step = EducationalRequest.REQUEST_STEPS[5]
            m.save()
        r.save()
        return redirect(reverse('educational:requests'))


@login_required
def request_single_remove(request, r_id):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            Message.objects.create(
                text=f'درخواست شما مبنی بر {r.title} توسط {request.user} رد شد',
                educational_request=None,
                owner=r.user,
                message_expert=request.user,
            ).save()
            # if request.user.user_permissions.filter(name__contains='register'):
            #     if r.register_status is False:
            #         r.reject = True
            #         r.final_status = False
            # elif request.user.user_permissions.filter(name__contains='financial'):
            #     if r.financial_status is False:
            #         r.reject = True
            #         r.final_status = False
            #     elif r.financial_status_2 is False:
            #         r.reject = True
            #         r.final_status = False
            # elif request.user.user_permissions.filter(name__contains='educational'):
            #     if r.educational_status is False:
            #         r.reject = True
            #         r.final_status = False
            #     elif r.educational_status_2 is False:
            #         r.reject = True
            #         r.final_status = False
            r.reject = True
            r.final_status = False
            r.step = EducationalRequest.REQUEST_STEPS[6]
            r.save()
    return redirect(reverse('educational:requests'))
