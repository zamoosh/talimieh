from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *

app_name = 'client'
urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', register, name="register"),
    path('logout/', Logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('user-document/', user_document, name="user_document"),
    path('user-document-upload/', user_document_upload, name="user_document_upload"),
    path('get-document/api/', get_document, name="get_document"),
    path('create-new-user/', create_new_staff_user, name='create_new_staff_user'),
    path('make-staff/<int:u_id>/', make_staff, name='make_staff'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
