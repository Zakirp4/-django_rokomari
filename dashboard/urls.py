from django.urls import path
from .views import writer_list, WriterListView, WriterDetailView, SubjectListView, SubjectDetailView, PublicationListView, PublicationDetailView

urlpatterns = [
    path('product/list', writer_list),
    path('writer/list', WriterListView.as_view(), name='writer_list'),
    path('subject/list', SubjectListView.as_view(), name='subject_list'),
    path('publication/list', PublicationListView.as_view(), name='publication_list'),

    path('writer/detail/<int:pk>', WriterDetailView.as_view(), name='writer_detail'),
    path('subject/detail/<int:pk>', SubjectDetailView.as_view(), name='subject_detail'),
    path('publication/detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
]