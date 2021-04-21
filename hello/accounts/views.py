from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, UserChangeForm, ProfileChangeForm
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin

# # Create your views here.
# def login_view(request, *args, **kwargs):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('project:list')
#         context['has_error'] = True
#     return render(request, 'registrations/login.html', context=context)
#
#
# @login_required
# def logout_view(request, *args, **kwargs):
#     logout(request)
#     return redirect('project:list')
#
# def register_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = MyUserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('project:list')
#     else:
#         form = MyUserCreationForm()
#     return render(request, 'registrations/user_create.html', context={'form': form})


def register_view(request, *args, **kwargs):
    context = {}
    form = MyUserCreationForm(data=request.POST)
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project:list')

    context['form'] = form
    return render(request, 'registration/user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserList(ListView):
    model = get_user_model()
    template_name = 'user_list.html'
    context_object_name = 'users'
    permission_required = 'webapp.view_user'

class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'usr_obj'
    profile_form_class = ProfileChangeForm

    def get_context_data(self, **kwargs):
        context = super(UserChangeView, self).get_context_data()
        context['profile_form'] = kwargs.get('profile_form')
        if context['profile_form'] is None:
            context['profile_form'] = self.get_profile_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()
        profile_form = self.get_profile_form()
        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)

    def get_object(self, queryset=None):
        self.request.user

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(
            form=user_form,
            profile_form=profile_form
        )
        return self.render_to_response(context)

    def form_valid(self, user_form, profile_form):
        response = super(UserChangeView, self).form_valid(user_form)
        profile_form.save()
        return response

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return self.profile_form_class(**form_kwargs)


    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': object.pk})
