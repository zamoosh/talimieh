from .imports import *


def submit_upload(request, r_id=None):
    return redirect(reverse('educational:uni_request_submit'))
