from django.urls import path
from . import views
urlpatterns = [
    path('school/', views.Schoolviews, name='school'),
    path('school/<int:pk>', views.SingleSchoolviews, name='singleschool'),
    path('create/', views.create_instanceviews, name='create_instance'),

    path('student/', views.studentViews, name='student'),
    path('student/<int:pk>', views.studentViews, name='single_student'),

    path('teacher/', views.TeacherViews.as_view(), name='teacher'),
    path('teacher/<int:pk>', views.TeacherViews.as_view(), name='single_teacher'),

    # using mixin views
    path('teachermixin/', views.TeacherMixinView.as_view(), name='teachermixin'),
    # single instance retrive, update delete
    path('singleteachermixin/<int:pk>', views.SingleTeacherMixinView.as_view(), name='singleteachermixin'),


]
