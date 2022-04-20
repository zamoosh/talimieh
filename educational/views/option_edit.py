from .imports import *


@login_required
def option_edit(request, o_id):
    if not (request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser):
        return redirect(reverse('page_not_found'))
    o = Option.objects.get(id=o_id)
    if request.method == 'GET':
        context = {}
        context['option'] = o
        return render(request, 'educational/option_edit.html', context)
    if request.method == 'POST':
        if request.POST.get('name'):
            o.name = request.POST.get('name')
        if request.POST.get('price'):
            o.price = request.POST.get('price')
        o.save()
        return redirect(reverse('educational:options'))
