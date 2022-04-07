from .imports import *


@login_required
def option_for_request(request, r_id):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    if request.method == 'POST':
        r = EducationalRequest.objects.get(id=r_id)
        checked_options = Option.objects.filter(id__in=request.POST.getlist('options'))
        common = r.selectedoption_set.filter(option__in=checked_options)
        delete = r.selectedoption_set.filter(~Q(option__in=checked_options))
        for item in delete:
            item.delete()
        add = []
        common_option = [item.option for item in common]
        for o in checked_options:
            if not (o in common_option):
                add.append(o)
        for o in add:
            s_o = SelectedOption.objects.create(option=o, request=r)
            s_o.save()
        request.session['option'] = True
        return redirect(reverse('educational:request_single_detail', kwargs={'r_id': r_id}))
