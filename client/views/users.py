from .imports import *
from client.models import User


def users(request):
    context = {'users': User.objects.all()}
    return render(request, 'client/users.html', context=context)
