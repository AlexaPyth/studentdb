# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_lector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ekzamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('duscuplina', models.CharField(verbose_name='Дисципліна', max_length=256)),
                ('data_ekzamena', models.DateTimeField(verbose_name='Дата і час іспиту', null=True, blank=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.Group', null=True, verbose_name='Група')),
            ],
            options={
                'verbose_name_plural': 'Екзамени',
                'verbose_name': ('Екзамен',),
            },
        ),
        migrations.AlterField(
            model_name='lector',
            name='birthday',
            field=models.DateField(verbose_name='Дата народження', help_text='yyyy-mm-dd', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ekzamen',
            name='lecktor',
            field=models.ForeignKey(to='students.Lector', null=True, verbose_name='Викладач-екзаменатор', blank=True, max_length=256),
        ),
    ]
