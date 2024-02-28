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

    # Update model instance
    def update(self, instance, validated_data):
        # if user can update data : save updated data. else save previous data.
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_duration = validated_data.get('course_duration', instance.course_duration)
        instance.seat = validated_data.get('seat', instance.seat)

        instance.save()

        return instance