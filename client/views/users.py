from .imports import *


def users(request):
    context = {}
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    if request.session.get('message'):
        context['message'] = True
        del request.session['message']
    context['users'] = User.objects.all()
    return render(request, 'client/users.html', context=context)
