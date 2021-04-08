"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from webapp.views import (
#     IndexView,
#     TaskView,
#     CreateTask,
#     UpdateTask,
#     DeleteTask,
#     ProjectView,
#     ProjectDetailView,
#     ProjectCreate,
#     ProjectUpdate,
#     ProjectDelete
#
# )
#
# urlpatterns = [
#     path('tracker/', IndexView.as_view(), name='list-task'),
#     path('<int:pk>/tracker/view/', TaskView.as_view(), name='view-task'),
#     path('<int:pk>/tracker/add/', CreateTask.as_view(), name='add-task'),
#     path('<int:pk>/tracker/update/', UpdateTask.as_view(), name='update-task'),
#     path('<int:pk>/tracker/delete/', DeleteTask.as_view(), name='delete-task'),
#     path('', ProjectView.as_view(), name='list-project'),
#     path('<int:pk>/', ProjectDetailView.as_view(), name='view-project'),
#     path('add/', ProjectCreate.as_view(), name='add-project'),
#     path('<int:pk>/update/', ProjectUpdate.as_view(), name='update-project'),
#     path('<int:pk>/delete/', ProjectDelete.as_view(), name='delete-project'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


HOMEPAGE_URL = 'webapp/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url=HOMEPAGE_URL, permanent=True)),
]
