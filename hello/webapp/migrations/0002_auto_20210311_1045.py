# Generated by Django 3.1.7 on 2021-03-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'статус', 'verbose_name_plural': 'статусы'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'тип', 'verbose_name_plural': 'типы'},
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
