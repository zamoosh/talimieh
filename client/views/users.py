from .imports import *


def users(request):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {'users': User.objects.all()}
    return render(request, 'client/users.html', context=context)
