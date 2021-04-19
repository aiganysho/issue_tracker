from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя',
        related_name='profile'
    )
    bith_date = models.DateField(
      null=True,
      blank=True,
      verbose_name='Дата рождения'
    )

    avatar = models.ImageField(
       null=True,
       blank=True,
       upload_to='avatars',
       verbose_name='Аватар'
    )

    about_yourself = models.TextField(max_length=2900, null=True, blank=True, verbose_name='О себе')
    link = models.URLField(max_length=299, null=True, blank=True, verbose_name='Профиль на GitHub')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table= 'profiles'
        verbose_name= 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'