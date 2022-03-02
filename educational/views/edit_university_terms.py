from .imports import *


def edit_university_terms(request, u_id):
    context = {}
    university = get_object_or_404(Universities, id=u_id)
    degree_list = []
    degree_selected = Semester.objects.values('degree_field_study__id').filter(university=university)
    for i in degree_selected:
        degree_list.append(i['degree_field_study__id'])
    degree_selected = DegreeFieldStudy.objects.filter(id__in=degree_list)
    context['request'] = {}
    context['request']['uni'] = university.id
    context['all_fields'] = DegreeFieldStudy.objects.all()
    context['degree_selected'] = degree_selected
    if request.method == 'POST':
        university = get_object_or_404(Universities, id=u_id)
        primary_semester = [item for item in university.semester_set.all()]
        select_semester = []
        for item in request.POST.getlist('degree'):
            degree = DegreeFieldStudy.objects.get(id=item)
            try:
                select_semester.append(degree.semester_set.get(university=university))
            except (Exception, Exception):
                select_semester.append(1)
        if len(select_semester) > len(primary_semester):
            for item in select_semester:
                if not (item in primary_semester):
                    try:
                        item.delete()
                    except (Exception, Exception):
                        None
        elif len(select_semester) < len(primary_semester):
            for item in primary_semester:
                if not (item in select_semester):
                    item.delete()
        context['request']['degree_list'] = request.POST.getlist('degree')
        request.session['degrees'] = context['request']
        if len(primary_semester) != len(select_semester):
            return redirect(reverse('educational:submit_semester'))
    return render(request, 'educational/uni_edit.html', context)
