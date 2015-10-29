# -*- coding: utf-8 -*-
__author__ = 'sasha'
from django.db import models


class Ekzamen(models.Model):
    '''
     назва предмету; дата і час проведення;
     назва викладача, що прийматиме іспит; група, для якої проводитиметься іспит.
    '''

    class Meta(object):
        verbose_name = 'Екзамен'
        verbose_name_plural = 'Екзамени'

    duscuplina = models.CharField(
        max_length=256,
        verbose_name='Дисципліна',
        blank=False)

    data_ekzamena = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата і час іспиту"
    )

    lecktor = models.ForeignKey(
        'Lector',
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Викладач-екзаменатор'
    )

    group = models.ForeignKey(
        'Group',
        verbose_name='Група',
        blank=True,
        null=True,
        on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.duscuplina, self.lecktor.last_name)
