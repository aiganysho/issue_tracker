from django import forms

from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ('summary', 'description', 'type', 'status')


# class ArticleDeleteForm(forms.Form):
#     title = forms.CharField(max_length=120, required=True, label='Введите название статьи, чтобы удалить её')