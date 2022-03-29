from .imports import *
from client.models import User


def user_perms(request, u_id):
    if request.user.is_superuser or request.user.user_permissions.filter(name__icontains='see'):
        if request.method == 'GET':
            u = User.objects.get(id=u_id)
            context = {}
            context['user'] = u
            context['admin_and_expert_perms'] = Permission.objects.filter(
                Q(codename__icontains='can_see') | Q(codename__icontains='can_set_expert')
            )
            return render(request, 'client/user_perms.html', context)
    else:
        return redirect(reverse('page_not_found'))


def user_set_perms(request, g_id, u_id):
    if request.method == 'POST':
        u = get_object_or_404(User, id=u_id)
        p = get_object_or_404(Permission, id=g_id)
        if p in u.user_permissions.all():
            u.user_permissions.remove(p)
            u.user_permissions.add(Permission.objects.get(name__contains='normal'))
        else:
            u.user_permissions.add(p)
            if u.user_permissions.filter(name__contains='normal'):
                u.user_permissions.remove(Permission.objects.get(name__contains='normal'))
        u.save()
    return redirect(reverse('client:user_perms', args=[u_id]))
