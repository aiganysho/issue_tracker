from django import forms

from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ('summary', 'description', 'type', 'status')


class TaskDeleteForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Enter name task , to delete!')