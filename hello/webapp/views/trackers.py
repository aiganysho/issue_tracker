from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode

from webapp.models import Task, Project
from webapp.form import TaskForm, SearchForm
from webapp.base_views import CustomFormView
# Create your views here.



class IndexView(ListView):
    template_name = 'tracker/index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('summary', '-created_at')
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context


class TaskView(TemplateView):

    template_name = 'tracker/task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class CreateTask(CreateView):
    template_name = 'tracker/task_create.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect(reverse('view-project', kwargs={'pk': project.pk}))



class UpdateTask(FormView):
    template_name = 'tracker/task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view-task', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class DeleteTask(TemplateView):
    template_name = 'tracker/task_delete.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('list-task')

