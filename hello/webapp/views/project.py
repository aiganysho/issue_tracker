from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView
from webapp.models import Project, Task
from webapp.form import ProjectForm

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


class ProjectCreate(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse(
            'view-project',
            kwargs={'pk': self.object.pk}
        )

