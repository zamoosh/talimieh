from .imports import *
from client.models import User
from django.contrib.auth.models import Permission


def user_perms(request):
    if request.method == 'GET':
        u = User.objects.get(id=request.GET.get('user_id'))
        context = {'user': u, 'user_perms': u.user_permissions.filter(name__contains='user')}
    return redirect(reverse('client:users'))
