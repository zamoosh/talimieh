from .imports import *


@login_required
def uni_degrees_show(request):
    if not (request.user.is_superuser or request.user.user_permissions.filter(name__icontains='see')):
        return redirect(reverse('page_not_found'))
    if request.GET.get('u'):
        context = {}
        uni = Universities.objects.get(id=request.GET.get('u'))
        sections_id = uni.semester_set.filter(degree_field_study__parent__isnull=False,
                                              status=True).values_list('degree_field_study__parent', flat=True)
        context['sections'] = []
        for section in DegreeFieldStudy.objects.filter(id__in=sections_id):
            context['sections'].append(
                {'id': section.id, 'title': section.title}
            )
        context['uni'] = uni
        return render(request, 'educational/uni_degrees_show.html', context)
    return redirect(reverse('educational:semesters'))
