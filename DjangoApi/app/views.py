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


@api_view(['GET'])
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