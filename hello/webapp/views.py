from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.models import Task
from webapp.form import TaskForm

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

class CreateTask(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        form = TaskForm()
        kwargs['form'] = form
        return super().get_context_data(**kwargs)

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
                type=form.cleaned_data.get('type')
            )
            return redirect('view-task', pk=task.id)
        return render(request, self.template_name, context={'form': form})


class UpdateTask(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description
        })
        kwargs['form'] = form
        kwargs['task'] = task
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary'),
            task.description = form.cleaned_data.get('description')
            task.save()
            return redirect('view-task', pk=kwargs.get('pk'))
        kwargs['form'] = form
        kwargs['task'] = task
        return render(request, self.template_name, context={'form': form, 'task': task})


class DeleteTask(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('list-task')

