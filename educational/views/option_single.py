from .imports import *


def option_single(request, o_id=None):
    if request.method == 'GET':
        return render(request, 'educational/option_create.html')
    if request.method == 'POST':
        o = Option.objects.create(name=request.POST.get('name'),
                                  price=request.POST.get('price'))
        o.save()
        return redirect(reverse('educational:options'))
