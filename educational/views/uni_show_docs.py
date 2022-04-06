from .imports import *


@login_required
def uni_show_docs(request, u_id):
    context = {}
    if request.method == "GET":
        if request.session.get('message'):
            context['message'] = True
            del request.session['message']
        context['uni'] = Universities.objects.get(id=u_id)
    return render(request, 'educational/uni_show_docs.html', context)
