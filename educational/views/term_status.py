from client.views.imports import *


def term_status(request, t_id):
    if request.method == 'POST':
        term = YearSemester.objects.get(id=t_id)
        if term.status:
            term.status = False
        else:
            term.status = True
        term.save()
        return redirect(reverse('educational:year_semester'))
    return redirect(reverse('educational:year_semester'))
