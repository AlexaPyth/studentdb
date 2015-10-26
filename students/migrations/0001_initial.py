# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=256, verbose_name='Прізвище')),
                ('middle_name', models.CharField(default='', max_length=256, verbose_name='По-батькові')),
                ('birthday', models.DateField(null=True, verbose_name='Дата народження')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('ticket', models.CharField(max_length=256, verbose_name='Білет')),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
        ),
    ]
