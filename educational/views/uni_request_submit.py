from .imports import *


@login_required
def uni_request_submit(request):
    context = {}
    if 'e_request' in request.session:
        context = request.session['e_request']
        context['uni_dic'] = Universities.objects.get(id=context['collage']).document
    context['semesters'] = Semester.objects.filter(status=True)
    u = User.objects.get(id=request.user.id)
    context['doc_len'] = len(u.ownerdocument_set.all())
    context['doc_con'] = True
    return render(request, 'educational/uni_request_submit.html', context)
