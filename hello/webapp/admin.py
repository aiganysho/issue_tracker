from django.contrib import admin
from webapp.models import Task, Status, Type, Project


# Register your models here.

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Task)
admin.site.register(Project)