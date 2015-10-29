# -*- coding: utf-8 -*-
__author__ = 'sasha'

from django.db import models

class Chell(models.Model):
    '''
    Задумка створити Батьківський клас
    для Студентів та викладачів
    '''

    class Meta(object):
        verbose_name = "Людина"
        verbose_name_plural = "Люди"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="По-батькові",
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name="Дата народження",
        null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)