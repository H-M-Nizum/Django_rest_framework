from django.shortcuts import render
from . models import SchoolModel
from . serializers import SchoolSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# Queryset
def Schoolviews(request):
    # complex data
    complex_data = SchoolModel.objects.all()

    #python dict or native data 
    native_data = SchoolSerializers(complex_data, many=True)
    # print(native_data)

    # render json
    json_data = JSONRenderer().render(native_data.data)

    # Json data send to user

    return HttpResponse(json_data, content_type = 'application/json')

# Model instance
def SingleSchoolviews(request, pk):
    # complex data
    complex_data = SchoolModel.objects.get(id=pk)

    #python dict or native data 
    native_data = SchoolSerializers(complex_data)
    # print(native_data)

    # render json
    json_data = JSONRenderer().render(native_data.data)

    # Json data send to user

    return HttpResponse(json_data, content_type = 'application/json')


# Create School model instance
@csrf_exempt
def create_instanceviews(request):
    if request.method == 'POST':
        # contain instance data
        json_data = request.body
        # convert json to stream
        stream_data = io.BytesIO(json_data)
        # convert stream to python data.
        pythondata = JSONParser().parse(stream_data)
        # convert python data to complex data
        complex_data = SchoolSerializers(data = pythondata)

        # save data
        if complex_data.is_valid():
            complex_data.save()
            message = {'msg' : 'Successfully insert data'}
            # convert message to json data
            json_message = JSONRenderer().render(message)
            return HttpResponse(json_message, content_type = 'application.json')
        json_message = JSONRenderer().render(complex_data.errors)
        return HttpResponse(json_message, content_type = 'application.json')
    
    if request.method == 'PUT':
        # contain instance data
        json_data = request.body
        # convert json to stream
        stream_data = io.BytesIO(json_data)
        # convert stream to python data.
        pythondata = JSONParser().parse(stream_data)

        # get instance id
        id = pythondata.get('id')
        try:
            object_instance = SchoolModel.objects.get(id=id)
            print(object_instance)
            # convert python data to complex data
            # partial=true means don't need to update total model instance
            complex_data = SchoolSerializers(object_instance, data = pythondata, partial=True)

            # save data
            if complex_data.is_valid():
                complex_data.save()
                message = {'msg' : 'Successfully insert data'}
                # convert message to json data
                json_message = JSONRenderer().render(message)
                return HttpResponse(json_message, content_type = 'application.json')
            json_message = JSONRenderer().render(complex_data.errors)
            return HttpResponse(json_message, content_type = 'application.json')
            
        except ObjectDoesNotExist:
            message = {'msg': 'This id is not available'}
            # convert message to json data
            json_message = JSONRenderer().render(message)

            return HttpResponse(json_message, content_type='application/json')

    # delete method
    if request.method == "DELETE":
        # contain instance data
        json_data = request.body
        # convert json to stream
        stream_data = io.BytesIO(json_data)
        # convert stream to python data.
        pythondata = JSONParser().parse(stream_data)

        # get instance id
        id = pythondata.get('id')
        try:
            object_instance = SchoolModel.objects.get(id=id)
            print(object_instance)

            # delete model instance
            object_instance.delete()

            message = {'msg': 'Successfully deleted data'}
            # convert message to json data
            json_message = JSONRenderer().render(message)

            return HttpResponse(json_message, content_type='application/json')

        except ObjectDoesNotExist:
            message = {'msg': 'This id is not available'}
            # convert message to json data
            json_message = JSONRenderer().render(message)

            return HttpResponse(json_message, content_type='application/json')



# #############################################################################################
# ###################### Class Based And Function Based Api Views #############################
# #############################################################################################

from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentViews(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            # complex data
            studentdata = StudentModel.objects.get(id=id)
            # Python dictonary data
            pythondata = StudentSerializers(studentdata)
            return Response(pythondata.data)

        studentdata = StudentModel.objects.all()
        pythondata = StudentSerializers(studentdata, many=True)
        return Response(pythondata.data)

    # POST method
    if request.method == "POST":
        serialierData = StudentSerializers(data = request.data)
        if serialierData.is_valid():
            serialierData.save()

            return Response({'msg' : 'Successfully insert data'})
        return Response(serialierData.errors)
    
    # PUT method  ## Full instance updated
    if request.method == "PUT":
        id = pk
        studentdata = StudentModel.objects.get(id=id)
        serialierData = StudentSerializers(studentdata, data = request.data)
        if serialierData.is_valid():
            serialierData.save()
            return Response({'msg' : 'successfully update data using put method'})
        return Response(serialierData.errors)

    # PATCH method  ## one or more fields updated
    if request.method == "PATCH":
        id = pk
        studentdata = StudentModel.objects.get(id=id)
        serialierData = StudentSerializers(studentdata, data = request.data, partial=True)
        if serialierData.is_valid():
            serialierData.save()
            return Response({'msg' : 'successfully update data using PATCH method'})
        return Response(serialierData.errors)

    # DELETE method
    if request.method == "DELETE":
        id = pk
        studentdata = StudentModel.objects.get(id=id)
        studentdata.delete()
        return Response({'msg' : 'Successfully delete data using DELETE method'})


# ############################# Class based APIVIews #######################

from rest_framework.views import APIView
from .models import TeacherModel
from .serializers import TeacherSerializers

class TeacherViews(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            teacherdata = TeacherModel.objects.get(id=id)
            pythondata = TeacherSerializers(teacherdata)
            return Response(pythondata.data)
        
        teacherdata = TeacherModel.objects.all()
        pythondata = TeacherSerializers(teacherdata, many=True)
        return Response(pythondata.data)


    # POST method
    def post(self, request, format=None):
        serializerdata = TeacherSerializers(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response({'msg' : 'Successfully create data'})
        return Response(serializerdata.errors)

    # PUT method
    def put(self, request, pk, format=None):
        id = pk
        teacherdata = TeacherModel.objects.get(id=id)
        pythondata = TeacherSerializers(teacherdata, data = request.data)

        if pythondata.is_valid():
            pythondata.save()
            return Response({'msg' : 'Update successfully using PUT method'})
        return Response(pythondata.errors)
    
    # PATCH method
    def patch(self, request, pk, format=None):
        id=pk
        teacherdata = TeacherModel.objects.get(id=id)
        pythondata = TeacherSerializers(teacherdata, data=request.data, partial=True)

        if pythondata.is_valid():
            pythondata.save()
            return Response({'msg' : 'Update successfully using PATCH mehod'})
        return Response(pythondata.errors)

    # DELETE method
    def delete(self, request, pk, format=None):
        id=pk
        deletedata = TeacherModel.objects.get(id=id)
        deletedata.delete()
        return Response({'msb' : 'Successfully delete data'})


# ###################### Using mixins in Django Rest Framework ###################

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class TeacherMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# single instance retrive, update delete
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
class SingleTeacherMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


########################################################################################
################## ListCreateAPIView And RetrieveUpdateDestroyAPIView ##################
########################################################################################

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class List_Create_APIView(ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

class Retrieve_Update_Destroy_APIView(RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers
