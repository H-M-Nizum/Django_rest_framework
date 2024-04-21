from django.urls import path, include
from .views import StudentView, StudentSessionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', StudentView, basename='student')
router.register('studentsession', StudentSessionView, basename='studentsession')
urlpatterns = [
    path('', include(router.urls)),

    # for login and logout option
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
