from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

class Type(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'


class Task(BaseModel):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок', validators=[MinLengthValidator(5), ])
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание', validators=[MinLengthValidator(10), ])
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks', null=False, blank=False)
    type = models.ManyToManyField('webapp.Type', related_name='tasks', blank=False)
    project = models.ForeignKey(
        'webapp.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        null=False,
        blank=False,
        default=1
    )
    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.summary}: {self.description}'


class Project(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description_project = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание проекта')
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    user = models.ManyToManyField(get_user_model(), related_name='projects', null=False, blank=False, verbose_name='Пользователь')

    class Meta:
        db_table = 'Projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        permissions = [
            ('have_user', 'есть пользователь')
        ]

    def __str__(self):
        return f'{self.id}: {self.name} {self.description_project}'
