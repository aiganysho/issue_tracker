from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project, Task
from webapp.form import ProjectForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectView(ListView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 10
    paginate_orphans = 1



class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    context_key = 'project'
    model = Project


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse(
            'project:view',
            kwargs={'pk': self.object.pk}
        )


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_key = 'project'
    def get_success_url(self):
        return reverse(
            'project:view',
            kwargs={'pk': self.object.pk}
        )



class ProjectDelete(LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('project:list')


