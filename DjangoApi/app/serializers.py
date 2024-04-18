from rest_framework import serializers
from .models import SchoolModel, StudentModel, TeacherModel

# Normal serializer
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


# Model serializer
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['student_name', 'class_name', 'age', 'roll']
        # fields = '__all__'  # Mean all fields in studentModel

# Model serializer for teacher model
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id', 'teacher_name', 'subject_name', 'age', 'salary']
        # fields = '__all__'  # Mean all fields in studentModel


from .models import FoodCategory, FoodItem

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'