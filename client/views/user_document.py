from .imports import *


def request_generator(user: 'user of djagno request', ids, data):
    r = EducationalRequest.objects.create(user=user,
                                          title=data['title'],
                                          average=data['average'],
                                          former_university=data['former_uni'],
                                          college=data['sem'])
    for item in ids:
        print(item)
        od = OwnerDocument.objects.get(id=item)
        r.ownerdocument_set.add(od)
    r.save()
    return r


def user_document(request):
    context = {'documents': OwnerDocument.objects.filter(user=request.user.id)}
    return render(request, 'client/user_document.html', context)


def user_document_upload(request):
    if request.method == "POST":
        data = {
            'title': request.POST.get('title'),
            'former_uni': request.POST.get('former_uni'),
            'average': request.POST.get('average'),
            'sem': Semester.objects.get(id=request.POST.get('sem')),
            'field_study': request.POST.get('field_study')
        }
        request_generator(request.user, request.POST.getlist('images'), data)
        return HttpResponseRedirect(reverse('educational:uni_request_submit'))
    return redirect(reverse('educational:uni_request_submit'))
