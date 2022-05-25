from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from educational.models import OwnerDocument, User


@csrf_exempt
def image_uploader(request):
    accepted_types = ['png', 'jpg', 'jpeg', 'pdf', 'word']
    if request.method == 'POST':
        file = request.FILES['file'].read()
        file_name = request.POST['filename']
        existing_path = request.POST['existingPath']
        end = request.POST['end']
        next_slice = request.POST['nextSlice']

        if file == "" or file_name == "" or existing_path == "" or end == "" or next_slice == "":
            res = JsonResponse({'data': 'Invalid Request'})
            return res
        else:
            if existing_path == 'null':
                image = OwnerDocument()
                image.title = request.POST.get('title')
                image.image.name = file_name
                image.user = request.user
                image.save()
                path = os.path.join(settings.MEDIA_ROOT, 'document', str(image.id), file_name)
                if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'document', str(image.id))):
                    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'document', str(image.id)))
                    os.chmod(os.path.join(settings.MEDIA_ROOT, 'document', str(image.id)), 0o755)
                with open(path, 'wb+') as destination:
                    destination.write(file)
                image.image.name = os.path.join('document', str(image.id), file_name)
                image.save()
                if int(end):
                    res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': image.image.name})
                    if not image.image.name.split('.')[-1] in accepted_types:
                        print('not accepted!')
                        res = JsonResponse({'data': 'فایل تائید نشد'})
                else:
                    res = JsonResponse({'existingPath': image.image.name})
                return res

            else:
                path = os.path.join(settings.MEDIA_ROOT, existing_path)
                model_id = OwnerDocument.objects.get(image=existing_path)
                if model_id.image.name.split("/")[-1] == file_name:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination:
                            destination.write(file)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': model_id.image.name})
                        else:
                            res = JsonResponse({'existingPath': model_id.image.name})
                        return res
                    else:
                        res = JsonResponse({'data': 'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data': 'No such file exists in the existingPath'})
                    return res
    return render(request, '/')
    # if request.method == 'POST':
    #     file = request.FILES['file']
    #     f = request.FILES['image']
    #     img_name = request.POST['filename']
    #     existingPath = request.POST['existingPath']
    #     end = request.POST['end']
    #     nextSlice = request.POST['nextSlice']
    #     # os.makedirs(os.path.join(settings.MEDIA_ROOT, 'document', str(request.user.id)), exist_ok=True)
    #     if file == "" or img_name == "" or existingPath == "" or end == "" or nextSlice == "":
    #         res = JsonResponse({'data': 'Invalid Request'})
    #         return res
    #     else:
    #         if existingPath == 'null':
    #             # path = os.path.join(settings.MEDIA_ROOT, 'document', str(o.id), img_name)
    #             # with open(path, 'wb+') as destination:
    #             #     destination.write(file)
    #             u = User.objects.get(id=request.user.id)
    #             o = OwnerDocument.objects.create(
    #                 title=request.POST['title'],
    #                 user=u,
    #                 image=f
    #             )
    #             o.save()
    #             # owner_doc = OwnerDocument()
    #             # owner_doc.existingPath = os.path.join('document', str(request.user.id), img_name)
    #             # owner_doc.eof = end
    #             # owner_doc.title = os.path.join('document', str(request.user.id), img_name)
    #             # owner_doc.user = u
    #             # owner_doc.save()
    #             if int(end):
    #                 res = JsonResponse({'data': 'Uploaded Successfully',
    #                                     'existingPath': os.path.join('document', str(request.user.id), img_name)})
    #             else:
    #                 res = JsonResponse({'existingPath': os.path.join('document', str(request.user.id), img_name)})
    #             return res
    #
    #         else:
    #             path = os.path.join(settings.MEDIA_ROOT, 'document', str(request.user.id), img_name)
    #             model_id = OwnerDocument.objects.get(existingPath=existingPath)
    #             if model_id.name == os.path.join('document', str(request.user.id), img_name):
    #                 if not model_id.eof:
    #                     with open(path, 'ab+') as destination:
    #                         destination.write(file)
    #                     if int(end):
    #                         model_id.eof = int(end)
    #                         model_id.save()
    #                         res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': model_id.existingPath})
    #                     else:
    #                         res = JsonResponse({'existingPath': model_id.existingPath})
    #                     return res
    #                 else:
    #                     res = JsonResponse({'data': 'EOF found. Invalid request'})
    #                     return res
    #             else:
    #                 res = JsonResponse({'data': 'No such file exists in the existingPath'})
    #                 return res
    # return render(request, f'admin/{__name__.split(".")[0]}/{__name__.split(".")[-1]}.html')
