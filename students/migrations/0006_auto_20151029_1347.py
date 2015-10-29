# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20151029_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ekzamen',
            options={'verbose_name_plural': 'Екзамени', 'verbose_name': 'Екзамен'},
        ),
        migrations.AlterField(
            model_name='ekzamen',
            name='group',
            field=models.ForeignKey(to='students.Group', null=True, verbose_name='Група', blank=True, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
