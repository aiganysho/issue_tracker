from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin

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


class TaskView(DetailView):
    model = Task
    template_name = 'tracker/task_view.html'



class CreateTask(LoginRequiredMixin, CreateView):
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



class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tracker/task_update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('view-task', kwargs={'pk': self.kwargs.get('pk')})



class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tracker/task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('list-task')



