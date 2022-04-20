from django.urls import path
from .views import *

app_name = 'educational'

urlpatterns = [
    path('universities/', universities, name="universities"),

    path('year-semester/', year_semester, name="year_semester"),
    path('year_semester/api/', get_year, name="get_year"),
    path('term_status/<int:t_id>', term_status, name="term_status"),

    path('degree-field-study/', degree_field_study, name="degree_field_study"),
    path('create-degree-section/', create_degree_section, name="create_degree_section"),
    path('get_degree_field_sections/api/', get_degree_field_sections, name='get_degree_field_sections'),
    path('get_section/api/', get_section, name='get_section'),

    path('semesters/', semesters, name="semesters"),
    path('new-semester/', new_semester, name="new_semester"),
    path('submit-semester/', submit_semester, name="submit_semester"),

    path('semester/api/', if_any_semester_active, name="if_any_semester_active"),
    path('get_degree/api/<int:t_id>/', get_degree, name="get_degree"),
    path('have-section/api/', have_section, name='have_section'),
    path('get_degree_semesters/', get_degree_semesters, name='get_degree_semesters'),

    path('upload-new-doc/', upload_new_doc, name='upload_new_doc'),
    path('submit-upload/', submit_upload, name='submit_upload'),

    path('uni-reqest/', uni_request, name="uni_request"),
    path('uni/api/', get_uni, name="get_uni"),
    path('get-uni-for-request/api/', get_uni_for_request, name='get_uni_for_request'),
    path('uni/api/has-semester/', uni_has_semester, name='uni_has_semester'),
    path('uni-reqest-submit/', uni_request_submit, name="uni_request_submit"),
    path('uni-edit/<int:u_id>', edit_university_terms, name='uni_edit_terms'),
    path('uni-degrees-show/', uni_degrees_show, name='uni_degrees_show'),
    path('uni-edit-docs/<int:u_id>/', uni_edit_docs, name='uni_edit_docs'),
    path('uni-show-docs/<int:u_id>/', uni_show_docs, name='uni_show_docs'),

    path('reports/', reports, name='reports'),

    path('requests/', requests, name='requests'),
    path('requests/<str:message>/', requests, name='requests_with_message'),
    path('request-single/<int:r_id>/', request_single_confirm, name='request_single_confirm'),
    path('request-single-detail/', request_single_detail, name='request_single_detail'),
    path('request-single-remove/<int:r_id>/', request_single_remove, name='request_single_remove'),
    path('request-single-transitions/api/', get_transaction_of_educational_request, name='request_single_transition'),

    path('options/', options, name='options'),
    path('option-single-create/', option_single_create, name='option_single_create'),
    path('option-single-delete/<int:o_id>/', option_single_delete, name='option_single_delete'),
    path('option-single-edit/<int:o_id>/', option_edit, name='option_single_edit'),
]
