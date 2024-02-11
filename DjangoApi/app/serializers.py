from rest_framework import serializers
from .models import SchoolModel

class SchoolSerializers(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=50)
    course_name = serializers.CharField(max_length=50)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    # create model instance
    def create(self, validated_data):
        return SchoolModel.objects.create(**validated_data)