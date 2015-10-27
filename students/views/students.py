# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models import Student
#from students.views.my_pagination import MyPaginator

#  Було на старті для Тестування
# students = (
#         {'id':1,
#          'first_name': 'Андрій',
#          'last_name': 'Корост',
#          'ticket': 2123,
#          'image': 'img/me.jpg'},
#         {'id':2,
#          'first_name': 'Орест',
#          'last_name': 'Пивовар',
#          'ticket': 2125,
#          'image': 'img/piv.jpg'},
#         {'id': 3,
#          'first_name': 'Віталій',
#          'last_name': 'Пдоба',
#          'ticket': 2127,
#          'image': 'img/podoba.jpg'},
#     )

# Views for Students
def students_list(request):
    students = Student.objects.all().order_by('last_name')

    # try to order Student list
    order_by = request.GET.get('order_by')
    if order_by in ('id','last_name', "first_name", 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse') == '1':
            students = students.reverse()

    # paginate students From Books
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    # paginate students My
    # paginator = MyPaginator(students, 3)
    # page = request.GET.get('page')
    # students = paginator.page(page)



    return render(request, "students/students_list.html", {'students':students})

def students_add(request):
    # testa = request.META['SERVER_NAME']
    # print(request.build_absolute_uri('/'))
    return HttpResponse("Add students")

def students_edit(request, sid):
    return HttpResponse("Edit students %s" % sid)

def students_delete(request, sid):
    return HttpResponse("Delete students %s" % sid)
