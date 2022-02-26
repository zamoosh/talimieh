from .imports import *
from client.models import User


def create_new_staff_user(request):
    for u in User.objects.all():
        print(u.username, u.first_name, u.last_name)
    context = {'users': User.objects.all()}
    return render(request, 'client/create_new_staff_user.html', context=context)
