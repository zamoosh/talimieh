from .imports import *
from client.models import User


@login_required
def user_perms(request, u_id):
    if request.user.is_superuser or request.user.user_permissions.filter(name__icontains='see'):
        if request.method == 'GET':
            context = {}
            if request.session.get('message'):
                context['message'] = True
                del request.session['message']
            u = User.objects.get(id=u_id)
            context['user'] = u
            context['admin_and_expert_perms'] = Permission.objects.filter(
                Q(codename__icontains='can_see') | Q(codename__icontains='can_set_expert')
            )
            return render(request, 'client/user_perms.html', context)
    else:
        return redirect(reverse('page_not_found'))
