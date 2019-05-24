from django.contrib import admin
from .models import Student,Course
# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','sloc']

class AdminCourse(admin.ModelAdmin):
    list_display = ['cno','cname','cfee']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)