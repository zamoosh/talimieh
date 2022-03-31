from .imports import *


def semesters(request):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {'semesters': Semester.objects.filter(status=True).values_list('university', flat=True).distinct()}
    context['uni_semesters'] = Universities.objects.filter(id__in=context['semesters'])
    return render(request, 'educational/semesters.html', context)
