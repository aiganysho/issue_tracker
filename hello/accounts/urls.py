from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view, UserDetailView, UserList, UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('list/', UserList.as_view(), name='user-list'),
    path('profile/change/', UserChangeView.as_view(), name='user-change'),
    path('change-password/', UserPasswordChangeView.as_view(), name='user-password-change')
]