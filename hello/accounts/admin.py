from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileInline(admin.StackedInline):
    fields = ('bith_date', 'avatar', 'about_yourself', 'link')
    model = Profile


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
