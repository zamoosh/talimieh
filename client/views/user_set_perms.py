from .imports import *


@login_required
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
        request.session['message'] = True
    return redirect(reverse('client:user_perms', args=[u_id]))
