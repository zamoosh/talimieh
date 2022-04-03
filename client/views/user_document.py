from .imports import *


def request_generator(user: 'user of djagno request', ids, data):
    r = EducationalRequest.objects.create(user=user,
                                          title=data['title'],
                                          average=data['average'],
                                          former_university=data['former_uni'])
    for item in data['sems']:
        s = SelectedSemester.objects.create(semester=item, educational_request=r)
        s.save()
    for item in ids:
        od = OwnerDocument.objects.get(id=item)
        r.ownerdocument_set.add(od)
    r.tracking_code = str(user.id)
    r.save()


def user_document(request):
    context = {'documents': OwnerDocument.objects.filter(user=request.user.id)}
    return render(request, 'client/user_document.html', context)


def user_document_upload(request):
    if request.method == "POST":
        sem_list = []
        for item in request.POST.getlist('sem'):
            sem_list.append(Semester.objects.get(id=item))
        data = {}
        data['title'] = request.POST.get('title')
        data['former_uni'] = request.POST.get('former_uni')
        data['average'] = request.POST.get('average')
        data['sems'] = sem_list
        data['field_study'] = request.POST.get('field_study')
        request_generator(request.user, request.POST.getlist('images'), data)
        return redirect(reverse('educational:uni_request_submit'))
    return redirect(reverse('educational:uni_request_submit'))
