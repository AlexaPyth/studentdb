# -*- coding: utf-8 -*-
__author__ = 'sasha'
from django.db import models

""" Journal Model """

class Journal(models.Model):

    class Meta(object):
        verbose_name = "Журнал"
        verbose_name_plural = "Журнал"


    student = models.ForeignKey('Student',
        verbose_name="Студент(ФІ)",
        blank=False,
        on_delete=models.PROTECT)


