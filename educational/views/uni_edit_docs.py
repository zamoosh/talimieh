from .imports import *


@login_required
def uni_edit_docs(request, u_id):
    if request.method == 'POST':
        uni = Universities.objects.get(id=u_id)
        uni.document = json.dumps(request.POST.get('doc').split('\r\n'))
        uni.comment = json.dumps(request.POST.get('comment').split('\r\n'))
        uni.save()
        request.session['message'] = True
        return redirect(reverse('educational:uni_show_docs', kwargs={'u_id': u_id}))
