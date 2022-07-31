from django.shortcuts import redirect, reverse


def is_id_real(model, obj_id):
    if not model.objects.filter(id=obj_id).exists():
        return redirect(reverse('page_not_found'))
    pass
