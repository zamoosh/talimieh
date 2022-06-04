from .imports import *


@login_required
def document_pattern_list(request):
    context = {}
    if not request.user.is_superuser:
        return redirect(reverse('page_not_found'))
    context['document_patterns'] = DocumentPattern.objects.filter(status=True)
    return render(request, f'{__name__.replace("views.", "").replace(".", "/")}.html', context)
