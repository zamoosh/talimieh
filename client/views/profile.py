from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .imports import *
import jdatetime


@login_required
def profile(request):
    context = {}
    if request.method == "POST":
        context['req'] = {}
        context['req']['first_name'] = request.POST.get('first_name', '').strip()
        context['req']['last_name'] = request.POST.get('last_name', '').strip()
        context['req']['nationality'] = request.POST.get('nationality', '').strip()
        context['req']['father_name'] = request.POST.get('father_name', '').strip()
        context['req']['email'] = request.POST.get('email', '').strip()
        context['req']['ancestor_name'] = request.POST.get('ancestor_name', '').strip()
        context['req']['nick_name'] = request.POST.get('nick_name', '').strip()
        context['req']['pass_number'] = request.POST.get('pass_number', '').strip()
        context['req']['place_birth'] = request.POST.get('place_birth', '').strip()
        context['req']['place_issue'] = request.POST.get('place_issue', '').strip()
        context['req']['whatsapp'] = request.POST.get('whatsapp', '').strip()
        user = User.objects.get(id=request.user.id)
        user.first_login = False
        user.first_name = context['req']['first_name']
        user.last_name = context['req']['last_name']
        user.father_name = context['req']['father_name']
        user.email = context['req']['email']
        user.ancestor_name = context['req']['ancestor_name']
        user.nick_name = context['req']['nick_name']
        user.pass_number = context['req']['pass_number']
        user.place_birth = context['req']['place_birth']
        user.place_issue = context['req']['place_issue']
        user.whatsapp = context['req']['whatsapp']
        if request.POST.get('password'):
            if len(request.POST.get('password')) >= 8:
                user.set_password(request.POST.get('password'))
            else:
                return redirect('client:profile')
        if context['req']['nationality'] == "arabic":
            user.nationality = 0
        elif context['req']['nationality'] == "afghanistan":
            user.nationality = 1
        if request.POST.get('birth_date'):
            user.birth_date = request.POST.get('birth_date')
        if request.POST.get('pass_issue_date'):
            user.pass_issue_date = request.POST.get('pass_issue_date')
        if request.POST.get('pass_expiration'):
            user.pass_expiration = request.POST.get('pass_expiration')
        user.save()
        return HttpResponseRedirect(reverse('client:profile'))
    user = User.objects.get(id=request.user.id)
    if user.first_login is False:
        context['birth_date'] = user.birth_date.__str__()
        context['pass_issue_date'] = user.pass_issue_date.__str__()
        context['pass_expiration'] = user.pass_expiration.__str__()
    else:
        context['change_password'] = True
    return render(request, 'client/profile.html', context)
