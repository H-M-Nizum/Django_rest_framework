from django.contrib import admin
from . models import SchoolModel
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display =['id', 'teacher_name', 'course_name', 'course_duration', 'seat']
    
admin.site.register(SchoolModel, SchoolAdmin)

