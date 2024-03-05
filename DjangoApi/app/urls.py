from django.urls import path, include
from . import views

# for model views set
from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()
# Register
router.register('teacherset', views.ModelViewSetView, basename='teachermodel')

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

    # ListCreateAPIView, RetrieveUpdateDestroyAPIView
    path('teacherlistcreate/', views.List_Create_APIView.as_view(), name="teacherlistcreate"),
    path('teacherputdeleteretrive/<int:pk>', views.Retrieve_Update_Destroy_APIView.as_view(), name="teacherputdeleteretrive"),


    # Viewsets.ModelViewSet
    path('', include(router.urls)),
]
