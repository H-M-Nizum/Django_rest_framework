from django.contrib import admin
from . models import SchoolModel, StudentModel
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display =['id', 'teacher_name', 'course_name', 'course_duration', 'seat']
admin.site.register(SchoolModel, SchoolAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display =['id', 'student_name', 'class_name', 'age', 'roll'] 
admin.site.register(StudentModel, StudentAdmin)

