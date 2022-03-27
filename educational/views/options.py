from .imports import *


@login_required
def options(request):
    if request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser:
        context = {}
        context['options'] = Option.objects.all()
        return render(request, 'educational/options.html', context)
    return redirect(reverse('page_not_found'))
