# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=256, verbose_name='Прізвище')),
                ('middle_name', models.CharField(max_length=256, default='', verbose_name='По-батькові')),
                ('birthday', models.DateField(verbose_name='Дата народження', null=True)),
            ],
            options={
                'verbose_name_plural': 'Викладачі',
                'verbose_name': 'Викладач',
            },
        ),
    ]
