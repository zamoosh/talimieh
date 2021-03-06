from .imports import *


@login_required
def request_single_confirm(request, r_id):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    if request.method == 'POST' and r_id:
        user = User.objects.get(id=request.user.id)
        r = EducationalRequest.objects.get(id=r_id)
        if r.reject is False:
            m = Message.objects.create(
                text=f'درخواست شما توسط {user} تائید شد',
                educational_request=r,
                owner=r.user,
                message_expert=user,
            )
            if int(r.step[1]) == 1:
                r.request_expert_register = user
                r.step = EducationalRequest.REQUEST_STEPS[1]
            elif int(r.step[1]) == 2:
                r.request_expert_educational = user
                r.step = EducationalRequest.REQUEST_STEPS[2]
            elif int(r.step[1]) == 3:
                r.request_expert_financial = user
                r.step = EducationalRequest.REQUEST_STEPS[3]
            elif int(r.step[1]) == 4:
                r.request_expert_educational = user
                r.step = EducationalRequest.REQUEST_STEPS[4]
            elif int(r.step[1]) == 5:
                r.request_expert_financial = user
                r.step = EducationalRequest.REQUEST_STEPS[5]
                r.paid = True
            elif int(r.step[1]) == 6:
                r.request_expert_educational = user
                r.step = EducationalRequest.REQUEST_STEPS[6]
                r.final_status = True
                StudentCard.objects.create(educational_request=r).save()
            m.save()
        r.save()
        return redirect(reverse('educational:request_single_detail', kwargs={'r_id': r_id}))
