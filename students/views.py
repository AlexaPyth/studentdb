from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Views for Students
def students_list(request):
    return render(request, "students/students_list.html", {})

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