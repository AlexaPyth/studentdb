# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from students.models.groups import Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# groups = (
#     {'id': 1, 'group_name': 'МтМ-21', 'starosta': 'Ячменев Олег' },
#     {'id': 2, 'group_name': 'МтМ-22',  'starosta': 'Петров Семен'  },
#     {'id': 3, 'group_name': 'МтМ-23', 'starosta': 'Іванов Олег' },
# )


# Views for Groups
def groups_list(request):
    groups = Group.objects.all()

        # try to order Groups List
    order_by = request.GET.get('order_by')
    if order_by in ('id','title','leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse') == '1':
            groups = groups.reverse()

        # paginator Groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, "students/groups_list.html", {'groups':groups})

def groups_add(request):
    return HttpResponse("Groups add")

def groups_edit(request, gid):
    return HttpResponse("Groups edit %s" % gid)

def groups_delete(request, gid):
    return HttpResponse("Groups delete %s" % gid)