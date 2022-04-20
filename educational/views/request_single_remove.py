from .imports import *


@login_required
def request_single_remove(request, r_id):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    if request.method == 'POST':
        if r_id:
            r = EducationalRequest.objects.get(id=r_id)
            m = Message.objects.create(
                text=f'درخواست شما توسط {request.user} تائید شد',
                educational_request=None,
                owner=r.user,
                message_expert=request.user,
            )
            m.save()
            r.reject = True
            r.final_status = False
            r.step = EducationalRequest.REQUEST_STEPS[6]
            r.save()
    return redirect(reverse('educational:requests'))
