from django.contrib import admin
from students.models.students import Student
from students.models.groups import Group
from students.models.lector import Lector
from students.models.ekzamen import Ekzamen

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Lector)
admin.site.register(Ekzamen)
