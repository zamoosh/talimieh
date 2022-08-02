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
        if not context['req']['first_name'].isnumeric():
            user.first_name = context['req']['first_name']
        else:
            request.session['name_err'] = True
            return redirect(reverse('client:profile'))
        if not context['req']['last_name'].isnumeric():
            user.last_name = context['req']['last_name']
        else:
            request.session['last_name_err'] = True
            return redirect(reverse('client:profile'))
        user.father_name = context['req']['father_name']
        user.email = context['req']['email']
        user.ancestor_name = context['req']['ancestor_name']
        user.nick_name = context['req']['nick_name']
        # TODO: fix validation for passport number it should be unique
        if context['req']['pass_number'].isnumeric():
            if not context['req']['pass_number'] == user.pass_number:  # if not like the previous
                if not User.objects.filter(pass_number=context['req']['pass_number']).exists():  # if pass doesn't exist
                    user.pass_number = context['req']['pass_number']
                else:
                    request.session['pass_error'] = True
        else:
            request.session['pass_number_err'] = True
            return redirect(reverse('client:profile'))
        if not context['req']['place_birth'].isnumeric():
            user.place_birth = context['req']['place_birth']
        else:
            request.session['place_birth'] = True
            return redirect(reverse('client:profile'))
        if not context['req']['place_issue'].isnumeric():
            user.place_issue = context['req']['place_issue']
        else:
            request.session['place_issue'] = True
            return redirect(reverse('client:profile'))
        if context['req']['whatsapp'].isnumeric():
            user.whatsapp = request.POST.get('pre_number') + request.POST.get('whatsapp')
        else:
            request.session['whatsapp_err'] = True
            return redirect(reverse('client:profile'))
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
        request.session['confirm_changes'] = True
        return HttpResponseRedirect(reverse('client:profile'))
    user = User.objects.get(id=request.user.id)
    if user.first_login is False:
        context['birth_date'] = user.birth_date.__str__()
        context['pass_issue_date'] = user.pass_issue_date.__str__()
        context['pass_expiration'] = user.pass_expiration.__str__()
    elif user.admin_create:
        context['change_password'] = True
    if request.session.get('confirm_changes'):
        context['confirm_changes'] = True
        del request.session['confirm_changes']
    if request.session.get('name_err'):
        context['name_err'] = True
        del request.session['name_err']
    if request.session.get('last_name_err'):
        context['last_name_err'] = True
        del request.session['last_name_err']
    if request.session.get('pass_number_err'):
        context['pass_number_err'] = True
        del request.session['pass_number_err']
    if request.session.get('place_birth'):
        context['place_birth'] = True
        del request.session['place_birth']
    if request.session.get('place_issue'):
        context['place_issue'] = True
        del request.session['place_issue']
    if request.session.get('whatsapp_err'):
        context['whatsapp_err'] = True
        del request.session['whatsapp_err']
    if request.session.get('pass_error'):
        context['pass_error'] = True
        del request.session['pass_error']
    return render(request, 'client/profile.html', context)
