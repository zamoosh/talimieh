from .imports import *


@login_required
def uni_edit_docs(request, u_id):
    if request.method == 'POST':
        uni = Universities.objects.get(id=u_id)
        uni.document = request.POST.get('doc')
        uni.comment = request.POST.get('comment')
        uni.save()
        request.session['message'] = True
        return redirect(reverse('educational:uni_show_docs', kwargs={'u_id': u_id}))
