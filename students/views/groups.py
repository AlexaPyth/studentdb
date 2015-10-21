# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


groups = (
    {'id': 1, 'group_name': 'МтМ-21', 'starosta': 'Ячменев Олег' },
    {'id': 2, 'group_name': 'МтМ-22',  'starosta': 'Петров Семен'  },
    {'id': 3, 'group_name': 'МтМ-23', 'starosta': 'Іванов Олег' },
)


# Views for Groups
def groups_list(request):
    return render(request, "students/groups_list.html", {'groups':groups})

def groups_add(request):
    return HttpResponse("Groups add")

def groups_edit(request, gid):
    return HttpResponse("Groups edit %s" % gid)

def groups_delete(request, gid):
    return HttpResponse("Groups delete %s" % gid)