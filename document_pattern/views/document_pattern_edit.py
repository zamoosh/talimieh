from .imports import *


@login_required
def document_pattern_edit(request, doc_id):
    context = {}
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    d = DocumentPattern.objects.get(id=doc_id)
    if request.method == 'POST':
        if request.POST.get('types'):
            d.types['types'] = DocumentPattern.split_types(request.POST.get('types').split(' '))
        else:
            d.types['types'] = ['jpg', 'png', 'jpeg', 'gif', 'pdf', 'txt', 'word']
        if request.POST.get('document_type') == '1' or request.POST.get('document_type') == '2':
            d.document_type = request.POST.get('document_type')
            if d.document_type == '1':
                d.extra['width'] = None
                d.extra['height'] = None
        d.document_type = request.POST.get('document_type')
        if not request.POST.get('title'):
            return redirect(reverse('document_pattern:edit', kwargs={'doc_id': doc_id}))
        context['document_pattern'] = d
        response = render(request, f'{__name__.replace("views.", "").replace(".", "/")}.html', context)
        if request.POST.get('size'):
            if request.POST.get('size').isnumeric():
                d.size = math.ceil(int(request.POST.get('size')))
            else:
                context['numeric_error'] = True
                return response
        if request.POST.get('width'):
            if request.POST.get('width').isnumeric():
                d.extra['width'] = math.ceil(int(request.POST.get('width')))
            else:
                context['numeric_error'] = True
                return response
        if request.POST.get('height'):
            if request.POST.get('height').isnumeric():
                d.extra['height'] = math.ceil(int(request.POST.get('width')))
            else:
                context['numeric_error'] = True
                return response
        d.title = request.POST.get('title')
        d.description = request.POST.get('description')
        d.save()
        d.file = request.FILES.get('image')
        d.save()
        request.session['update'] = True
        return redirect(reverse('document_pattern:edit', kwargs={'doc_id': doc_id}))
    context['document_pattern'] = d
    if request.session.get('update'):
        context['update'] = True
        del request.session['update']
    return render(request, f'{__name__.replace("views.", "").replace(".", "/")}.html', context)
