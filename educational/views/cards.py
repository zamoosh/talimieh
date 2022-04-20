from .imports import *


@login_required
def cards(request, user_id):
    context = {}
    u = User.objects.get(id=user_id)
    if u.is_superuser or u.user_permissions.filter(name__icontains='educational'):
        context['cards'] = StudentCard.objects.all()
    elif u.user.user_permissions.filter(name__icontains='normal'):
        context['cards'] = StudentCard.objects.filter(educational_request__user=u)
    return render(request, 'educational/cards.html', context)
