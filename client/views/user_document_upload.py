from .imports import *


@login_required
def user_document_upload(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        r = EducationalRequest.objects.create(user=user,
                                              average=request.POST.get('average'),
                                              former_university=request.POST.get('former_university'),
                                              former_field_study=request.POST.get('former_field_study'))
        s = SelectedSemester.objects.create(semester=Semester.objects.get(id=request.POST.get('degree-semester')),
                                            educational_request=r)
        s.save()
        for item in request.POST.getlist('images'):
            od = OwnerDocument.objects.get(id=item)
            r.ownerdocument_set.add(od)
        r.tracking_code = str(r.id)
        r.save()
        request.session['message'] = True
        return redirect(reverse('educational:requests'))
    return redirect(reverse('educational:uni_request_submit'))
