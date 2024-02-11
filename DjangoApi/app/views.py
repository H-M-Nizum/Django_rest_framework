from django.shortcuts import render
from . models import SchoolModel
from . serializers import SchoolSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
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
