# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Views for Journal

students = (
        {'id':1,
         'first_name': 'Андрій',
         'last_name': 'Корост'},
        {'id':2,
         'first_name': 'Орест',
         'last_name': 'Пивовар'},
        {'id': 3,
         'first_name': 'Віталій',
         'last_name': 'Пдоба'},
    )



def journal(request):
    return render(request, "students/journal.html", {'students_j':students})