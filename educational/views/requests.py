from .imports import *


def requests(request):
    context = {'requests': EducationalRequest.objects.all()}
    return render(request, 'educational/requests.html')
