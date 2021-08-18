from django.contrib import admin
from .models import Department, Student, Lecturer
# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Lecturer)