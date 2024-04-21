from django.urls import path, include
from .views import StudentView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('student', StudentView, basename='student')
urlpatterns = [
    path('', include(router.urls))
]
