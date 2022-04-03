from .imports import *
from client.models import User


def user_perms(request, u_id):
    if request.method == 'GET':
        u = User.objects.get(id=u_id)
        context = {}
        context['user'] = u
        context['user_perms'] = Permission.objects.filter(
            Q(codename__icontains='can_see') | Q(codename__icontains='can_set_expert')
        )
        return render(request, 'client/user_perms.html', context)


def user_set_perms(request, g_id, u_id):
    if request.method == 'POST':
        u = get_object_or_404(User, id=u_id)
        p = get_object_or_404(Permission, id=g_id)
        if p in u.user_permissions.all():
            u.user_permissions.remove(p)
        else:
            u.user_permissions.add(p)
        u.save()
    return redirect(reverse('client:user_perms', args=[u_id]))
