from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm


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