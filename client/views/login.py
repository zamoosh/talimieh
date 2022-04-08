from .imports import *


def Login(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    context['error'] = False
    if request.method == 'POST':
        context['request'] = {}
        context['request']['cellphone'] = request.POST.get('cellphone', '').strip()
        context['request']['password'] = request.POST.get('password', '').strip()
        if User.objects.filter(cellphone=context['request']['cellphone']).exists():
            user = authenticate(request, username=context['request']['cellphone'],
                                password=context['request']['password'])
            if user is not None:
                print('user is not None')
                if user.is_active:
                    login(request, user)
                    if user.first_login:
                        return redirect(reverse('client:profile'))
                    if user.user_permissions.filter(name__icontains='normal'):
                        return redirect('client:profile')
                    if len(request.GET.get("next", "/")) == 0:
                        print('len == 0')
                        return HttpResponseRedirect("/")
                    print('len != 0')
                    return HttpResponseRedirect(request.GET.get("next", "/"))
            else:
                context['error'] = True
        else:
            context['error'] = True
    return render(request, 'client/login.html', context)
