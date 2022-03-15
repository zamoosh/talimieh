from .imports import *
from client.models import User


def user_perms(request, u_id):
    if request.method == 'GET':
        context = {}
        context['user'] = request.user
        context['user_perms'] = request.user.groups.all()
        context['groups'] = Group.objects.filter(
            (Q(name__contains='expert') | Q(name__contains='admin')) & ~Q(user=request.user))
        return render(request, 'client/user_perms.html', context)


def user_set_perms(request, g_id, u_id):
    if request.method == 'POST':
        u = get_object_or_404(User, id=u_id)
        g = get_object_or_404(Group, id=g_id)
        if g in u.groups.all():
            u.groups.remove(g)
        else:
            u.groups.add(g)
        u.save()
    return redirect(reverse('client:user_perms', args=[u_id]))
