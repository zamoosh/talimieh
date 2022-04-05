from .imports import *


@login_required
def request_single_remove(request, r_id):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            Message.objects.create(
                text=f'درخواست شما توسط {request.user} تائید شد',
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
