from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('writer/list', WriterListView.as_view(), name='writer_list'),
    path('subject/list', SubjectListView.as_view(), name='subject_list'),
    path('publication/list', PublicationListView.as_view(), name='publication_list'),

    path('writer/detail/<int:pk>', WriterDetailView.as_view(), name='writer_detail'),
    path('subject/detail/<int:pk>', SubjectDetailView.as_view(), name='subject_detail'),
    path('publication/detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),

    path('writer/create', WriterCreateView.as_view(), name='writer_create'),
    path('subject/create', SubjectCreateView.as_view(), name='subject_create'),
    path('publication/create', PublicationCreateView.as_view(), name='publication_create'),

    path('writer/edit/<int:pk>', WriterEditView.as_view(), name='writer_edit'),
    path('subject/edit/<int:pk>', SubjectEditView.as_view(), name='subject_edit'),
    path('publication/edit/<int:pk>', PublicationEditView.as_view(), name='publication_edit'),

    path('writer/delete/<int:pk>', WriterDeleteView.as_view(), name='writer_delete'),
    path('subject/delete/<int:pk>', SubjectDeleteView.as_view(), name='subject_delete'),
    path('publication/delete/<int:pk>', PublicationDeleteView.as_view(), name='publication_delete'),


]