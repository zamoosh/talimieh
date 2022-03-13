from django.urls import path
from .views import *

app_name = 'educational'

urlpatterns = [
    path('universities/', universities, name="universities"),

    path('year-semester/', year_semester, name="year_semester"),
    path('year_semester/api/', get_year, name="get_year"),
    path('term_status/<int:t_id>', term_status, name="term_status"),

    path('degree-field-study/', degree_field_study, name="degree_field_study"),

    path('semesters/', semesters, name="semesters"),
    path('new-semester/', new_semester, name="new_semester"),
    path('submit-semester/', submit_semester, name="submit_semester"),
    path('uni/api/', get_uni, name="get_uni"),
    path('semester/api/', if_any_semester_active, name="if_any_semester_active"),
    path('get_degree/api/<int:t_id>/', get_degree, name="get_degree"),
    path('uni/api/has-semester/', uni_has_semester, name='uni_has_semester'),
    path('upload-new-doc/', upload_new_doc, name='upload_new_doc'),
    path('submit-upload/', submit_upload, name='submit_upload'),

    path('uni-reqest/', uni_request, name="uni_request"),
    path('uni-reqest-submit/', uni_request_submit, name="uni_request_submit"),
    path('uni-edit/<int:u_id>', edit_university_terms, name='uni_edit_terms'),

    path('reports/', reports, name='reports'),

    path('requests/', requests, name='requests'),
    path('request-single/', request_single, name='request_single'),
    path('request-single/<int:r_id>/', request_single, name='request_single'),
]
