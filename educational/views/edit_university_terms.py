from .imports import *


def edit_university_terms(request, u_id):
    context = {}
    university = get_object_or_404(Universities, id=u_id)
    degree_list = []
    degree_selected = Semester.objects.values('degree_field_study__id').filter(university=university)
    for i in degree_selected:
        degree_list.append(i['degree_field_study__id'])
    degree_selected = DegreeFieldStudy.objects.filter(id__in=degree_list)
    context['r'] = {}
    context['university'] = university
    context['r']['uni'] = university.id
    context['all_fields'] = DegreeFieldStudy.objects.filter(status=True, parent__isnull=False)
    context['degree_selected'] = degree_selected
    if request.method == 'POST':
        university = get_object_or_404(Universities, id=u_id)
        selected_degree = []
        for item in request.POST.getlist('degree'):
            degree = DegreeFieldStudy.objects.get(id=item)
            selected_degree.append(degree)
        common = university.semester_set.filter(degree_field_study__in=selected_degree)
        delete = university.semester_set.filter(~Q(degree_field_study__in=selected_degree))
        for item in delete:
            item.delete()
        add = []
        common_degree = []
        for item in common:
            common_degree.append(item.degree_field_study)
        for item in selected_degree:
            if not (item in common_degree):
                add.append(item)
        for item in add:
            sem = Semester.objects.create(university=university,
                                          degree_field_study=item,
                                          year_semester=YearSemester.objects.get(status=True))
            sem.save()
        context['r']['degree_list'] = request.POST.getlist('degree')
        request.session['degrees'] = context['r']
        return redirect(reverse('educational:submit_semester'))
    return render(request, 'educational/uni_edit.html', context)
