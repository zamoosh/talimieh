from .imports import *


def new_semester(request):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {}
    if request.method == 'POST':
        context['request'] = {}
        context['request']['uni'] = request.POST.get('uni', '').strip()
        context['request']['degree_list'] = request.POST.getlist('degree_list')
        for item in request.POST.getlist('degree_list'):
            uni = Universities.objects.get(id=context['request']['uni'])
            degree = DegreeFieldStudy.objects.get(id=item)
            sem = Semester.objects.create(university=uni,
                                          degree_field_study=degree,
                                          year_semester=YearSemester.objects.get(status=True))
            sem.save()
            print(item, sem)
        request.session['degrees'] = context['request']
        return HttpResponseRedirect(reverse('educational:submit_semester'))
    context['any_semester_active'] = YearSemester.objects.filter(status=True).exists()
    return render(request, 'educational/new_semester.html', context)
