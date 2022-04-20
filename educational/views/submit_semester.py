from pip._internal.cli import status_codes

from .imports import *


@login_required
def submit_semester(request):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {}
    if 'degrees' in request.session:
        context = request.session['degrees']
        context['degree_list'] = context['degree_list']
        context['uni'] = context['uni']
        context['university'] = Universities.objects.get(id=context['uni'])
        context['degree_fields'] = DegreeFieldStudy.objects.filter(id__in=context['degree_list'])
        context['year'] = YearSemester.objects.get(yearsemester__status=True)
        context['term'] = YearSemester.objects.get(parent=context['year'], status=True)
        if request.method == "POST":
            detail = {}
            for i in request.POST.items():
                if 'entrance_price_' in i[0]:
                    if i[0][len('entrance_price_'):] not in detail:
                        detail[i[0][len('entrance_price_'):]] = {}
                    if 'scholarship' not in detail[i[0][len('entrance_price_'):]]:
                        detail[i[0][len('entrance_price_'):]]['scholarship'] = False
                    detail[i[0][len('entrance_price_'):]]['entrance_price'] = i[1]
                if 'scholarship_' in i[0]:
                    if i[0][len('scholarship_'):] not in detail:
                        detail[i[0][len('scholarship_'):]] = {}
                    detail[i[0][len('scholarship_'):]]['scholarship'] = True
                if 'expert_price_' in i[0]:
                    if i[0][len('expert_price_'):] not in detail:
                        detail[i[0][len('expert_price_'):]] = {}
                    if 'scholarship' not in detail[i[0][len('expert_price_'):]]:
                        detail[i[0][len('expert_price_'):]]['scholarship'] = False
                    detail[i[0][len('expert_price_'):]]['expert_price'] = i[1]
            for i in context['degree_fields']:
                if str(i.id) in detail:
                    if i.semester_set.filter(university=context['university'], status=True):
                        for sem in i.semester_set.filter(university=context['university'], status=True):
                            sem.expert_price = detail[str(i.id)]['expert_price']
                            sem.entrance_price = detail[str(i.id)]['entrance_price']
                            sem.scholarship = detail[str(i.id)]['scholarship']
                            sem.save()
            return redirect(reverse('educational:semesters'))
        uni = Universities.objects.get(id=context['uni'])
        uni.save()
    # return render(request, f'{app_name.name}/{__name__.split(".")[-1]}.html', context)
    return render(request, 'educational/submit_semester.html', context)
