from .imports import *


def request_generator(user: 'user of djagno request', ids, data):
    r = EducationalRequest.objects.create(user=user,
                                          average=data['average'],
                                          former_university=data['former_university'],
                                          former_field_study=data['former_field_study'])
    s = SelectedSemester.objects.create(semester=Semester.objects.get(id=data['sem_id']), educational_request=r)
    s.save()
    for item in ids:
        od = OwnerDocument.objects.get(id=item)
        r.ownerdocument_set.add(od)
    r.tracking_code = str(user.id)
    r.save()


@login_required
def user_document(request):
    context = {}
    context['documents'] = OwnerDocument.objects.filter(user=request.user.id)
    context['amount_of_doc'] = request.user.ownerdocument_set.all().__len__()
    return render(request, 'client/user_document.html', context)


@login_required
def user_document_upload(request):
    if request.method == "POST":
        data = {}
        data['former_university'] = request.POST.get('former_university')
        data['former_field_study'] = request.POST.get('former_field_study')
        data['average'] = request.POST.get('average')
        data['sem_id'] = request.POST.get('degree-semester')
        data['field_study'] = request.POST.get('field_study')
        request_generator(request.user, request.POST.getlist('images'), data)
        return redirect(reverse('educational:requests'))
    return redirect(reverse('educational:uni_request_submit'))
