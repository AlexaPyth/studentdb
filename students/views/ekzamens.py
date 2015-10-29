# -*- coding: utf-8 -*-
__author__ = 'sasha'

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models.ekzamen import Ekzamen


# Views for Students
def ekzamens_list(request):
    ekzamens = Ekzamen.objects.all()  # .order_by('last_name')

    # try to order Student list
    order_by = request.GET.get('duscuplina', 'data_ekzamena')
    if order_by in ('duscuplina', 'data_ekzamena', 'lecktor', 'group'):
        ekzamens = ekzamens.order_by(order_by)
        if request.GET.get('reverse') == '1':
            students = ekzamens.reverse()

    # paginate students From Books
    paginator = Paginator(ekzamens, 3)
    page = request.GET.get('page')
    try:
        ekzamens = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ekzamens = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        ekzamens = paginator.page(paginator.num_pages)
    # students['x'] = (list(range(students.start_index(), students.end_index())))
    # paginate students My
    # paginator = MyPaginator(students, 3)
    # page = request.GET.get('page')
    # students = paginator.page(page)



    return render(request,"students/ekzamens_list.html",{'otvetka':ekzamens})


def ekzamens_add(request):
    # testa = request.META['SERVER_NAME']
    # print(request.build_absolute_uri('/'))
    return HttpResponse("Add ekzamen")


def ekzamens_edit(request, kid):
    return HttpResponse("Edit ekzamen %s" % kid)


def ekzamens_delete(request, kid):
    return HttpResponse("Delete ekzamen %s" % kid)
