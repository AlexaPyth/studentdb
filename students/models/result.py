# -*- coding: utf-8 -*-
__author__ = 'sasha'

from django.db import models

class Result_exam(models.Model):
    duscuplina = models.ForeignKey(
        'Ekzamen',
         verbose_name='Дисципліна',
         blank=False)

    student = models.ForeignKey(
        "Student",
         verbose_name='Студент',
         blank=False)

    ocinka_exam = models.IntegerField(
        verbose_name='Оцінка',
        blank=True )

    '''
додаткове завдання: реалізувати також результати іспитів.
Кожен результат прив’язується до іспиту та студента полями зв’язку і звісно
має оцінку. Користувацький інтерфейс і структура URL адрес тут буде дещо
складніша.
        '''