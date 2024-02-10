from django.urls import path
from . import views
urlpatterns = [
    path('school/', views.Schoolviews, name='school')
]
