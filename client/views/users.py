from .imports import *


def users(request):
    if is_normal(request):
        return render(request, '404_page.html')
    context = {'users': User.objects.all().order_by('id')}
    return render(request, 'client/users.html', context=context)
