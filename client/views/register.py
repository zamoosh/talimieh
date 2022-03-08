from django.urls import reverse
from .imports import *


def register(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    context['error'] = 0
    if request.method == "POST":
        context['request'] = {}
        context['request']['cellphone'] = request.POST.get('cellphone', '').strip()
        context['request']['password'] = request.POST.get('password', '').strip()
        if len(context['request']['cellphone']) < 11:
            context['cellphoneNum'] = 1
            context['error'] = 1
        if context['request']['password']:
            context['Strength'] = pwStrength(context['request']['password'])
            if context['Strength'] < 60:
                context['error'] = 1
                context['passconfilict'] = 1
        elif context['request']['password'] != request.POST.get('password2', ''):
            context['passconfilict'] = 1
            context['error'] = 1
        if context['error'] == 0:
            user = User.objects.create_user(
                cellphone=context['request']['cellphone'],
                username=context['request']['cellphone'],
                password=context['request']['password']
            )
            user.groups.add(Group.objects.get(name='normal student'))
            user.save()
            context['register'] = 1
            if context['register']:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/accounts/profile/")
    return render(request, 'client/register.html', context)
