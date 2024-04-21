from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework import viewsets

# for Authentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# for Permission
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

# Create  views for BasicAuthentication.
class StudentView(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    ## for basic authentication
    authentication_classes = [BasicAuthentication]
    ## for authenticated user permission
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]


# Create views for SessionAuthentication
class StudentSessionView(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    ## for basic authentication
    authentication_classes = [SessionAuthentication]
    ## for authenticated user permission
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]
