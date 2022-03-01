from .imports import *


def edit_university_terms(request, u_id):
    if request.method == 'POST':
        university = get_object_or_404(Universities, id=u_id)
        selected = []
        final = []
        for item in request.POST.getlist('semester'):
            selected.append(item)
        for item in university.semester_set.all():
            final.append(item)
        if len(final) < len(selected):
            for item in final:
                item.university = None
                item.save()
            for item in selected:
                s = Semester.objects.get(id=item)
                s.university = university
                s.save()
        elif len(final) > len(selected):
            i = 0
            while True:
                if not final:
                    break
                if selected:
                    if Semester.objects.get(id=selected[i]) in final:
                        final.remove(Semester.objects.get(id=selected[i]))
                        selected.pop(i)
                        i -= 1
                else:
                    break
                i += 1
            for item in final:
                item.university = None
                item.save()
        return redirect(reverse('educational:semesters'))
    university = get_object_or_404(Universities, id=u_id)
    uni_semesters = []
    for field in Degree_field_study.objects.all():
        for semester in field.semester_set.all():
            if university.id == semester.university.id:
                uni_semesters.append(semester)
    for dg in Degree_field_study.objects.all():
        for se in uni_semesters:
            if se in dg.semester_set.all():
                print(se)
            else:
                print(dg)
    context = {
        'uni': university,
        'uni_terms': uni_semesters,
        'all_fields': Degree_field_study.objects.all()
    }
    return render(request, 'educational/uni_edit.html', context)
