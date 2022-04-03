from .imports import *


@login_required
def option_single_create(request):
    if request.method == 'GET':
        return render(request, 'educational/option_create.html')
    if request.method == 'POST':
        o = Option.objects.create(name=request.POST.get('name'),
                                  price=request.POST.get('price'))
        o.save()
        return redirect(reverse('educational:options'))


@login_required
def option_single_delete(request, o_id):
    if request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser:
        if o_id:
            o = Option.objects.get(id=o_id)
            o.delete()
    return redirect(reverse('educational:options'))
