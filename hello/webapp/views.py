from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from webapp.models import Task
from webapp.form import TaskForm, TaskDeleteForm

# Create your views here.



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)

class TaskView(TemplateView):

    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

def task_create_view(request):

    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description')
            )
            return redirect('view-task', pk=task.id)
        return render(request, 'task_create.html', context={'form': form})

def task_update_view(request, pk):

    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary'),
            task.description = form.cleaned_data.get('description')
            task.save()
            return redirect('article-view', pk=task.id)

        return render(request, 'task_update.html', context={'form': form, 'task': task })


def task_delete_view(request, pk):

    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskDeleteForm()
        return render(request, 'task_delete.html', context={'task': task, 'form': form})
    elif request.method == 'POST':
        form = TaskDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['summary'] != task.summary:
                form.errors['summary'] = ['Названия статей не совпадают']
                return render(request, 'task_delete.html', context={'task': task, 'form': form})

            task.delete()
            return redirect('list-task')
        return render(request, 'task_delete.html', context={'task': task, 'form': form})
