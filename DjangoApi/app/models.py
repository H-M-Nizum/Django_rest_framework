from django.db import models

# Create your models here.

# Create complex data
class SchoolModel(models.Model):
    teacher_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    course_duration = models.IntegerField()
    seat = models.IntegerField()

class StudentModel(models.Model):
    student_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll = models.IntegerField()

class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name