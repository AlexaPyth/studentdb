# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from students.models.students import Student
from students.models.groups import Group
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
    students = Student.objects.all()  #.order_by('last_name')

    # try to order Student list
    order_by = request.GET.get('order_by','last_name')
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
    # students['x'] = (list(range(students.start_index(), students.end_index())))
    # paginate students My
    # paginator = MyPaginator(students, 3)
    # page = request.GET.get('page')
    # students = paginator.page(page)



    return render(request, "students/students_list.html", {'otvetka':students})

def students_add(request):
    # testa = request.META['SERVER_NAME']
    # print(request.build_absolute_uri('/'))
    '''         Метакод
         Якщо форма була запощена:
    Якщо кнопка Скасувати була натиснута:
        Повертаємо користувача до списку студентів
    Якщо кнопка Додати була натиснута:
        Перевіряємо дані на коректність та збираємо помилки
    Якщо дані були введені некоректно:
        Віддаємо шаблон форми разом із знайденими помилками
    Якщо дані були введені коректно:
        Створюємо та зберігаємо студента в базу
        Повертаємо користувача до списку студентів
     Якщо форма не була запощена:
        повертаємо код початкового стану форми
    '''
    # was form Posted?
    if request.method =='POST':
        # was form add button clicked?
        if request.POST.get('add_button') is not None:

            # TODO: validate input from user
            # error colections
            errors = {}

            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'note': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Ім'я є обовязковим "
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обовязковим "
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = "Дата народження є обовязковою "
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = 'Введіть коректний формат дати (напр. 1975-10-28)'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = "Номер білета є обовязковим "
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = 'Оберіть групу для студента'
            else:
                groups = Group.objects.filter(pk = student_group)
                if len(groups) !=1:
                    errors['student_group'] = "Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save student
            if not errors:
                student = Student(**data)  # як варіант через перевірку словника errors

                # create Student Object  - вважаєм що всі дані внесенно і вони правильні!
                # student = Student(
                #     first_name = request.POST['first_name'],
                #     last_name = request.POST['last_name'],
                #     middle_name = request.POST['middle_name'],
                #     birthday = request.POST['birthday'],
                #     ticket = request.POST['ticket'],
                #     student_group = Group.objects.get(pk = request.POST['student_group']),
                #     photo = request.FILES['photo'],
                # )

                # save it to database
                student.save()

                # redirect user to student list
                return HttpResponseRedirect('%s?status_message=Студента успішно додано!' % reverse('home'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cansel_button') is not None:
            # redirect to home page on Cansel Button
            return HttpResponseRedirect('%s?status_message=Додавання студента скасовано!' % reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                     {'groups' : Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse("Edit students %s" % sid)

def students_delete(request, sid):
    return HttpResponse("Delete students %s" % sid)
