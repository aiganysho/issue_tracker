from django import forms
from django.forms import ModelForm
from webapp.models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('summary', 'description', 'type', 'status')

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description_project', 'start_date', 'end_date')


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('user',)