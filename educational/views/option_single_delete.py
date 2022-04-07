from .imports import *


@login_required
def option_single_delete(request, o_id):
    if request.user.user_permissions.filter(name__icontains='see') or request.user.is_superuser:
        if o_id:
            o = Option.objects.get(id=o_id)
            o.delete()
    return redirect(reverse('educational:options'))
