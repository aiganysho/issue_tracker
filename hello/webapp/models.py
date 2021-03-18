from django.db import models
from django.core.validators import MinLengthValidator


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
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок', validators=[MinLengthValidator(10), ])
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание', validators=[MinLengthValidator(20), ])
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks', null=False, blank=False)
    type = models.ManyToManyField('webapp.Type', related_name='tasks', null=False, blank=False)

    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.summary}: {self.description}'



