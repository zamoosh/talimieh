from .imports import *


def request_single_detail(request):
    if request.GET.get('r'):
        r = EducationalRequest.objects.get(id=request.GET.get('r'))
        context = {}
        context['r'] = r
        context['selected_semesters'] = r.selectedsemester_set.all()
        context['user'] = r.user
        context['documents'] = r.ownerdocument_set.all()
        context['amount_of_doc'] = r.ownerdocument_set.all().__len__()
        context['r_con'] = False
        context['e_con'] = False
        context['f_con'] = False
        context['e_con_2'] = False
        context['f_con_2'] = False
        context['e_con_3'] = False
        if r.reject is False and (
                request.user.is_superuser or request.user.user_permissions.filter(name__contains='see')):
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
        return render(request, 'educational/request_single.html', context)
