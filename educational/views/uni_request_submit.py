from .imports import *


@login_required
def uni_request_submit(request):
    context = {}
    if 'e_request' in request.session:
        context = request.session['e_request']
        context['uni_dic'] = Universities.objects.get(id=context['collage']).document
    # context['unis'] = Universities.objects.filter(semester__in=Semester.objects.all())
    context['semesters'] = Semester.objects.filter(status=True)
    return render(request, 'educational/uni_request_submit.html', context)
