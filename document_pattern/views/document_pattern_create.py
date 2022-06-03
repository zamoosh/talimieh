from .imports import *


@login_required
def document_pattern_create(request):
    context = {}
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    if request.method == 'POST':
        d = DocumentPattern()
        if request.POST.get('types'):
            d.types['types'] = d.split_types(request.POST.get('types').split(' '))
        else:
            d.types['types'] = ['png', 'jpg', 'jpeg']
        d.title = request.POST.get('title')
        d.description = request.POST.get('description')
        d.save()
        context['save'] = True
        return redirect(reverse('document_pattern:edit', kwargs={'doc_id': d.id}))
    return render(request, f'{__name__.replace("views.", "").replace(".", "/")}.html', context)
