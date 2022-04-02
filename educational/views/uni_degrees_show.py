from .imports import *


@login_required
def uni_degrees_show(request):
    if not (request.user.is_superuser or request.user.user_permissions.filter(name__icontains='see')):
        return redirect(reverse('page_not_found'))
    if request.GET.get('u'):
        context = {}
        uni = Universities.objects.get(id=request.GET.get('u'))
        context['uni'] = uni
        return render(request, 'educational/uni_degrees_show.html', context)
    return redirect(reverse('educational:semesters'))
