from django.urls import path
from .views import *

app_name = 'document_pattern'

urlpatterns = [
    path('', document_pattern_list, name='list'),
    path('create/', document_pattern_create, name='create'),
    path('edit/<int:doc_id>/', document_pattern_edit, name='edit'),
    path('delete/<int:doc_id>/', document_pattern_delete, name='delete'),
]
