from django.contrib import admin
from .models import Writer, Subject, Publication

# Register your models here.
admin.site.register(Writer)
admin.site.register(Subject)
admin.site.register(Publication)