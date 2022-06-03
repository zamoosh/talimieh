from .imports import *


@login_required
def document_pattern_edit(request, doc_id):
    context = {}
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    d = DocumentPattern.objects.get(id=doc_id)
    if request.method == 'POST':
        if request.POST.get('types'):
            d.types['types'] = d.split_types(request.POST.get('types').split(' '))
        else:
            d.types['types'] = ['png', 'jpg', 'jpeg']
        if not request.POST.get('title'):
            return redirect(reverse('document_pattern:edit', kwargs={'doc_id': doc_id}))
        d.title = request.POST.get('title')
        d.description = request.POST.get('description')
        d.save()
        request.session['update'] = True
        return redirect(reverse('document_pattern:edit', kwargs={'doc_id': doc_id}))
    context['document_pattern'] = d
    if request.session.get('update'):
        context['update'] = True
        del request.session['update']
    print(d.title)
    return render(request, f'{__name__.replace("views.", "").replace(".", "/")}.html', context)
