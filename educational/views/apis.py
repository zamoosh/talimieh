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
    for i in Universities.objects.filter(status=True):
        context.append({'id': i.pk, 'title': i.uni_name, 'status': i.register_status})
    return JsonResponse(context, safe=False)


@login_required
def uni_has_semester(request):
    context = []
    for i in Universities.objects.filter(semester__isnull=False):
        context.append({'id': i.pk, 'title': i.uni_name, 'status': i.register_status})
    return JsonResponse(context, safe=False)


@login_required
def get_degree(request, t_id):
    context = []
    for i in Semester.objects.filter(university=t_id):
        context.append(
            {'id': i.pk, 'title': i.degree_field_study.title, 'uni': i.university.uni_name, 'bors': i.scholarship})
    return JsonResponse(context, safe=False)
