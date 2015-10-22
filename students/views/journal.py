# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Views for Journal
def journal(request):
    return render(request, "students/journal.html", {})