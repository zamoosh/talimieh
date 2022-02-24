from .imports import *


@login_required()
def year_semester(request):
    context = {}
    context['year_semesters'] = Year_semester.objects.filter(status=True).order_by('-id')
    if request.method == "POST":
        context['req'] = {}
        context['req']['year'] = request.POST.get('year', '').strip()
        print(context['req']['year'])
        context['req']['term'] = request.POST.get('term', '').strip()
        print(context['req']['term'])
        semester_year = Year_semester()
        semester_year.title = context['req']['year']
        semester_year.status = True
        if context['req']['term']:
            semester_year.parent_id = context['req']['term']
        semester_year.save()
    if 'remove' in request.GET:
        context['rmYear'] = Year_semester.objects.get(id=int(request.GET.get('remove')))
        context['rmYear'].status = 0
        context['rmYear'].save()
        context['remove'] = True
    return render(request, 'educational/year_semester.html', context)
