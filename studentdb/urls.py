"""studentdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from students.views.students import StudentUpdateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Students-list urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),

    #Groups List urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
        url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'),

    #Journal
    url(r'^journal/$', 'students.views.journal.journal', name='journal'),

    #Ekzamen List urls
    url(r'^ekzamens/$', 'students.views.ekzamens.ekzamens_list', name='ekzamens'),
    url(r'^ekzamens/add/$', 'students.views.ekzamens.ekzamens_add', name='ekzamens_add'),
    url(r'^ekzamens/(?P<kid>\d+)/edit/$', 'students.views.ekzamens.ekzamens_edit', name='ekzamens_edit'),
    url(r'^ekzamens/(?P<kid>\d+)/delete/$', 'students.views.ekzamens.ekzamens_delete', name='ekzamens_delete'),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),

]
#для підключення MEDIA_ROOT
from studentdb.settings import MEDIA_ROOT, DEBUG
if DEBUG:
# serve files from media folder
    urlpatterns.append (url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))
