from .imports import *


@login_required
def cards(request, user_id):
    context = {}
    return render(request, 'educational/cards.html', context)
