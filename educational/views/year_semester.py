from .imports import *


@login_required()
def year_semester(request):
    context = {'year_semesters': YearSemester.objects.all()}
    if request.method == "POST":
        context['req'] = {
            'year': request.POST.get('year', '').strip(),
            'term': request.POST.get('term', '').strip()
        }
        semester_year = YearSemester()
        semester_year.title = context['req']['year']
        if context['req']['term']:
            semester_year.parent_id = context['req']['term']
        semester_year.save()
    counter = 0
    for item in YearSemester.objects.all():
        if counter > 1:
            break
        if hasattr(item.parent, 'title'):
            if item.status:
                counter += 1
    if counter > 1:
        context['msg'] = True
        return render(request, 'educational/year_semester.html', context)
    if 'remove' in request.GET:
        try:
            y = YearSemester.objects.get(id=int(request.GET.get('remove')))
            y.delete()
        except (YearSemester.DoesNotExist, Exception):
            return render(request, 'educational/year_semester.html', context)
    return render(request, 'educational/year_semester.html', context)
