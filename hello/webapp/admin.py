from django.contrib import admin
from webapp.models import Task, Status, Type


# Register your models here.

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['id', 'status', 'type', 'summary', 'description', 'created_at', 'updated_at']
#     list_filter = ['status', 'summary']
#     search_fields = ['status', 'type']
#     fields = ['id', 'status', 'type', 'summary', 'description', 'created_at', 'updated_at']
#     readonly_fields = ['created_at', 'updated_at', 'id']


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Task)