from django.urls import path
from . import views
urlpatterns = [
    path('school/', views.Schoolviews, name='school'),
    path('school/<int:pk>', views.SingleSchoolviews, name='singleschool'),
    path('create/', views.create_instanceviews, name='create_instance'),
]
