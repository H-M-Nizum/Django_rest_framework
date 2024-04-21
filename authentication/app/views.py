from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework import viewsets
# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
