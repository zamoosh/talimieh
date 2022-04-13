from .imports import *


def submit_student_num(request, u_id, r_id):
    u = User.objects.get(id=u_id)
    u.student_num = request.POST.get('std_num')
    u.save()
    return redirect(reverse('educational:request_single_detail', kwargs={'r_id': r_id}))
