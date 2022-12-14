# Generated by Django 4.1 on 2022-09-11 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0004_remove_project_project_users_project_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='note_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project', verbose_name='Проект заметки'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор заметки'),
        ),
    ]
