from .imports import *


@login_required
def user_delete(request, u_id):
    if request.user.is_superuser or request.user.user_permissions.filter(name__icontains='set'):
        if request.method == 'POST' and u_id:
            u = User.objects.get(id=u_id)
            u.delete()
    request.session['message'] = True
    return redirect(reverse('client:users'))
