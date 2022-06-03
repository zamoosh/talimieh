from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from educational.models import OwnerDocument, User
import os


@csrf_exempt
def image_uploader(request):
    accepted_types = ['png', 'jpg', 'jpeg', 'pdf', 'word']
    if request.method == 'POST':
        file = request.FILES['file'].read()
        file_name = request.POST['filename']
        if not file_name.split('.')[-1] in accepted_types:
            return JsonResponse({'data': 'لطفا فرمت مناسب را انتخاب کنید!'}, status=400)
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
    return JsonResponse({'data': 'nothing'}, status=200)
