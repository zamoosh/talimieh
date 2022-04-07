from .imports import *


@login_required
def option_for_request(request, r_id):
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
        return redirect(reverse('educational:requests'))
