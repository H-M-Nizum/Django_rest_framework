from django.shortcuts import render
from . models import SchoolModel
from . serializers import SchoolSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
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