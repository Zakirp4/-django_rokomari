from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from product.forms import *



def dashboard(request):
    # writers = Writer.objects.all()
    return render(request, 'dashboard/dashboard.html')

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


class WriterCreateView(CreateView):
    model = Writer
    form_class = WriterForm
    success_url = reverse_lazy('writer_list')
    template_name = 'dashboard/writer_form.html'


class WriterEditView(UpdateView):
    model = Writer
    fields = '__all__'
    success_url = reverse_lazy('writer_list')
    template_name = 'dashboard/writer_form.html'


class WriterDeleteView(DeleteView):
    model = Writer
    success_url = reverse_lazy('writer_list')
    template_name = 'dashboard/writer_confirm_delete.html'


class SubjectListView(ListView):
    model = Subject
    template_name = 'dashboard/subject_list.html'
    context_object_name = 'subjects'


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'dashboard/subject_detail.html'
    context_object_name = 'subject'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy('subject_list')
    template_name = 'dashboard/subject_form.html'


class SubjectEditView(UpdateView):
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('subject_list')
    template_name = 'dashboard/subject_form.html'


class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')
    template_name = 'dashboard/subject_confirm_delete.html'


class PublicationListView(ListView):
    model = Publication
    template_name = 'dashboard/publication_list.html'
    context_object_name = 'publications'


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'dashboard/publication_detail.html'
    context_object_name = 'publication'

class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('publication_list')
    template_name = 'dashboard/publication_form.html'


class PublicationEditView(UpdateView):
    model = Publication
    fields = '__all__'
    success_url = reverse_lazy('publication_list')

    template_name = 'dashboard/publication_form.html'


class PublicationDeleteView(DeleteView):
    model = Publication
    success_url = reverse_lazy('publication_list')
    template_name = 'dashboard/publication_confirm_delete.html'





