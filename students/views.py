from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Views for Students
def students_list(request):
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
        {'id':1,
         'first_name': 'Віталій',
         'last_name': 'Пдоба',
         'ticket': 2127,
         'image': 'iimg/podoba.jpg'},
    )
    return render(request, "students/students_list.html", {'students':students})

def students_add(request):
    return HttpResponse("Add students")

def students_edit(request, sid):
    return HttpResponse("Edit students %s" % sid)

def students_delete(request, sid):
    return HttpResponse("Delete students %s" % sid)

# Views for Groups
def groups_list(request):
    return HttpResponse("Groups list")

def groups_add(request):
    return HttpResponse("Groups add")

def groups_edit(request, gid):
    return HttpResponse("Groups edit %s" % gid)

def groups_delete(request, gid):
    return HttpResponse("Groups delete %s" % gid)

#Views for Journal