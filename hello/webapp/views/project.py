from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Project, Task
from webapp.form import ProjectForm, ProjectUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


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


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse(
            'project:view',
            kwargs={'pk': self.object.pk}
        )


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_key = 'project'
    permission_required = 'webapp.change_project'
    def get_success_url(self):
        return reverse(
            'project:view',
            kwargs={'pk': self.object.pk}
        )



class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('project:list')
    permission_required = 'webapp.delete_project'




class AddUser(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user/user_create.html'
    form_class = ProjectUserForm
    context_object_name = 'project'
    permission_required = 'webapp.add_user'

    def get_success_url(self):
        return reverse(
            'project:view',
            kwargs={'pk': self.object.pk}
        )

    def has_permission(self):
            return super().has_permission() and self.request.user in Project.objects.get(
            pk=self.kwargs.get('pk')).user.all()


