# Generated by Django 3.1.7 on 2021-04-19 09:27

from django.conf import settings
from django.db import migrations, models

def create_profiles(apps, schema_editor):

    User = apps.get_model('auth', 'User')

    Profile = apps.get_model('accounts', 'Profile')

    for user in User.objects.all():

        Profile.objects.get_or_create(user=user)



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0010_auto_20210415_1050'),
    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]