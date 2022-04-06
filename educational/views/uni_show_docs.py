from .imports import *


@login_required
def uni_show_docs(request, u_id):
    context = {}
    if request.method == "GET":
        context['uni'] = Universities.objects.get(id=u_id)
    return render(request, 'educational/uni_show_docs.html', context)
