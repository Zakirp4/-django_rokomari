from django import forms
from .models import Writer, Subject, Publication


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'