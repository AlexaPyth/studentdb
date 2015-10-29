# -*- coding: utf-8 -*-
__author__ = 'sasha'

from django.db import models


class Lector(models.Model):
    class Meta(object):
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

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
        blank=True,
        verbose_name="Дата народження",
        null=True,
        help_text='yyyy-mm-dd')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
