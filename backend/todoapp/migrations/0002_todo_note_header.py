# Generated by Django 4.1 on 2022-08-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='note_header',
            field=models.CharField(max_length=64, null=True, verbose_name='Заголовок заметки'),
        ),
    ]
