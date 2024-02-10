from django.db import models

# Create your models here.

# Create complex data
class SchoolModel(models.Model):
    teacher_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    course_duration = models.IntegerField()
    seat = models.IntegerField()