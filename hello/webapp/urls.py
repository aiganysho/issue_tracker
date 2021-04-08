from django.urls import path
from webapp.views import (
    IndexView,
    TaskView,
    CreateTask,
    UpdateTask,
    DeleteTask,
    ProjectView,
    ProjectDetailView,
    ProjectCreate,
    ProjectUpdate,
    ProjectDelete

)

urlpatterns = [
    path('tracker/', IndexView.as_view(), name='list-task'),
    path('<int:pk>/tracker/view/', TaskView.as_view(), name='view-task'),
    path('<int:pk>/tracker/add/', CreateTask.as_view(), name='add-task'),
    path('<int:pk>/tracker/update/', UpdateTask.as_view(), name='update-task'),
    path('<int:pk>/tracker/delete/', DeleteTask.as_view(), name='delete-task'),
    path('', ProjectView.as_view(), name='list-project'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='view-project'),
    path('add/', ProjectCreate.as_view(), name='add-project'),
    path('<int:pk>/update/', ProjectUpdate.as_view(), name='update-project'),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name='delete-project'),
]
