from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Writer, Subject, Publication


def writer_list(request):
    writers = Writer.objects.all()
    return render(request, 'dashboard/writer_list.html', {'writers': writers})


class WriterListView(ListView):
    model = Writer
    template_name = 'dashboard/writer_list.html'
    context_object_name = 'writers'


class WriterDetailView(DetailView):
    model = Writer
    template_name = 'dashboard/writer_detail.html'
    context_object_name = 'writer'


class SubjectListView(ListView):
    model = Subject
    template_name = 'dashboard/subject_list.html'
    context_object_name = 'subjects'


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'dashboard/subject_detail.html'
    context_object_name = 'subject'


class PublicationListView(ListView):
    model = Publication
    template_name = 'dashboard/publication_list.html'
    context_object_name = 'publications'


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'dashboard/publication_detail.html'
    context_object_name = 'publication'


