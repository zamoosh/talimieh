from .imports import *


@login_required
def semesters(request):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {}
    semesters_id = Semester.objects.filter(status=True).values_list('university', flat=True).distinct()
    context['unis'] = Universities.objects.filter(id__in=semesters_id, status=True)
    return render(request, 'educational/semesters.html', context)
