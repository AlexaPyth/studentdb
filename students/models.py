from django.db import models


# Create your models here.
class Student(models.Model):
    """ Student Model """
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="��'�")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="�������")

    middle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="��-�������",
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name="���� ����������",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name="����",
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="�����")

    notes = models.TextField(
        blank=True,
        verbose_name="�������� �������",

    )

