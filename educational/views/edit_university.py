from .imports import *


def edit_university(request, u_id):
    university = Universities.objects.get(id=u_id)
    if request.method == 'POST':
        university.uni_name = request.POST.get('name')
        university.comment = request.POST.get('dec')
        university.document = request.POST.get('docs')
        university.save()
        return redirect(reverse('educational:universities'))
    context = {'uni': university}
    return render(request, 'educational/uni_edit.html', context)
