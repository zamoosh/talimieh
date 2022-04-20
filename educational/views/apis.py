from .imports import *


@login_required
def get_year(request, term=None):
    context = []
    for i in YearSemester.objects.filter(parent=term):
        context.append({'id': i.pk, 'year': i.title})
    return JsonResponse(context, safe=False)


@login_required
def if_any_semester_active(request):
    if YearSemester.objects.filter(status__exact=True).exists():
        return JsonResponse(True, safe=False)
    return JsonResponse(False, safe=False)


@login_required
def get_uni(request):
    context = []
    for i in Universities.objects.filter(semester__isnull=True, status=True):
        context.append({'id': i.pk, 'title': i.uni_name, 'status': i.status})
    return JsonResponse(context, safe=False)


@login_required
def get_uni_for_request(request):
    context = []
    for i in Universities.objects.filter(semester__isnull=False).distinct():
        context.append({'id': i.pk, 'name': i.uni_name})
    return JsonResponse(context, safe=False)


@login_required
def uni_has_semester(request):
    context = []
    for i in Universities.objects.filter(semester__isnull=False, status=True):
        context.append({'id': i.pk, 'title': i.uni_name, 'status': i.register_status})
    return JsonResponse(context, safe=False)


@login_required
def get_degree(request, t_id):
    context = []
    for i in Semester.objects.filter(university=t_id, status=True):
        context.append(
            {'id': i.pk, 'title': i.degree_field_study.title, 'uni': i.university.uni_name, 'bors': i.scholarship}
        )
    return JsonResponse(context, safe=False)


@login_required
def get_transaction_of_educational_request(request, er_id):
    context = {}
    e = EducationalRequest.objects.get(id=er_id)
    context['request_step'] = e.get_step()
    context['e_expert'] = e.request_expert_educational
    context['f_expert'] = e.request_expert_financial
    context['r_expert'] = e.request_expert_register
    return JsonResponse(context, safe=False)


@login_required
def get_degree_field_sections(request):
    context = []
    if request.method == 'POST' and request.POST.get('u_id'):
        u = Universities.objects.get(id=request.POST.get('u_id'))
        sections_id = u.semester_set.filter(degree_field_study__parent__isnull=False,
                                            status=True).values_list('degree_field_study__parent', flat=True)
        for section in DegreeFieldStudy.objects.filter(id__in=sections_id):
            context.append(
                {'id': section.id, 'title': section.title}
            )
        return JsonResponse(context, safe=False)


@login_required
def get_section(request):
    context = []
    sections = DegreeFieldStudy.objects.filter(parent__isnull=True, status=True)
    for item in sections:
        context.append(
            {'id': item.id, 'title': item.title}
        )
    return JsonResponse(context, safe=False)


@login_required
def get_degree_semesters(request):
    section = DegreeFieldStudy.objects.get(id=request.POST.get('d_id'))
    degrees = DegreeFieldStudy.objects.filter(parent=section)
    sem_list = []
    for degree in degrees:
        for sem in degree.semester_set.all():
            sem_list.append(
                {'id': sem.id, 'title': sem.__str__()}
            )
    return JsonResponse(sem_list, safe=False)


@login_required
def get_sections_degrees(request):
    section = DegreeFieldStudy.objects.get(id=request.POST.get('d_id'))
    degrees = DegreeFieldStudy.objects.filter(parent=section)
    sem_list = []
    for degree in degrees:
        sem_list.append(
            {'id': degree.id, 'title': degree.__str__()}
        )
    return JsonResponse(sem_list, safe=False)


@login_required
def have_section(request):
    return JsonResponse(DegreeFieldStudy.objects.filter(parent__isnull=True).exists(), safe=False)
