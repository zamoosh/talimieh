from .imports import *


@login_required
def option_edit(request, o_id):
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
