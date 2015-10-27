# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Назва', max_length=256)),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
            options={
                'verbose_name_plural': 'Групи',
                'verbose_name': 'Група',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Студенти', 'verbose_name': 'Студент'},
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Староста', null=True, blank=True, to='students.Student'),
        ),
    ]
