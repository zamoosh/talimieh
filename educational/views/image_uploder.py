from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from educational.models import OwnerDocument, User


@csrf_exempt
def image_uploader(request):
    if request.method == 'POST':
        file = request.FILES['file']
        f = request.FILES['image']
        img_name = request.POST['filename']
        existingPath = request.POST['existingPath']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']
        # os.makedirs(os.path.join(settings.MEDIA_ROOT, 'document', str(request.user.id)), exist_ok=True)
        if file == "" or img_name == "" or existingPath == "" or end == "" or nextSlice == "":
            res = JsonResponse({'data': 'Invalid Request'})
            return res
        else:
            if existingPath == 'null':
                # path = os.path.join(settings.MEDIA_ROOT, 'document', str(o.id), img_name)
                # with open(path, 'wb+') as destination:
                #     destination.write(file)
                u = User.objects.get(id=request.user.id)
                o = OwnerDocument.objects.create(
                    title=request.POST['title'],
                    user=u,
                    image=f
                )
                o.save()
                # owner_doc = OwnerDocument()
                # owner_doc.existingPath = os.path.join('document', str(request.user.id), img_name)
                # owner_doc.eof = end
                # owner_doc.title = os.path.join('document', str(request.user.id), img_name)
                # owner_doc.user = u
                # owner_doc.save()
                if int(end):
                    res = JsonResponse({'data': 'Uploaded Successfully',
                                        'existingPath': os.path.join('document', str(request.user.id), img_name)})
                else:
                    res = JsonResponse({'existingPath': os.path.join('document', str(request.user.id), img_name)})
                return res

            else:
                path = os.path.join(settings.MEDIA_ROOT, 'document', str(request.user.id), img_name)
                model_id = OwnerDocument.objects.get(existingPath=existingPath)
                if model_id.name == os.path.join('document', str(request.user.id), img_name):
                    if not model_id.eof:
                        with open(path, 'ab+') as destination:
                            destination.write(file)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': model_id.existingPath})
                        else:
                            res = JsonResponse({'existingPath': model_id.existingPath})
                        return res
                    else:
                        res = JsonResponse({'data': 'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data': 'No such file exists in the existingPath'})
                    return res
    return render(request, f'admin/{__name__.split(".")[0]}/{__name__.split(".")[-1]}.html', context)
