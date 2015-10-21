# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


students = (
        {'id':1,
         'first_name': 'Андрій',
         'last_name': 'Корост',
         'ticket': 2123,
         'image': 'img/me.jpg'},
        {'id':2,
         'first_name': 'Орест',
         'last_name': 'Пивовар',
         'ticket': 2125,
         'image': 'img/piv.jpg'},
        {'id': 3,
         'first_name': 'Віталій',
         'last_name': 'Пдоба',
         'ticket': 2127,
         'image': 'img/podoba.jpg'},
    )

# Views for Students
def students_list(request):
    return render(request, "students/students_list.html", {'students':students})

def students_add(request):
    # testa = request.META['SERVER_NAME']
    # print(request.build_absolute_uri('/'))
    return HttpResponse("Add students")

def students_edit(request, sid):
    return HttpResponse("Edit students %s" % sid)

def students_delete(request, sid):
    return HttpResponse("Delete students %s" % sid)
