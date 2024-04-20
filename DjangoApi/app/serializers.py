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
    
    # Field Level Validation : def validate_fieldName(self, value)
    def validate_seat(self, value):
        if value > 50:
            raise serializers.ValidationError('Seat must lessthen or equal to 50')
        if value < 20:
            raise serializers.ValidationError('Seat must Greater then 20')
        return value

    # Object Level Validation :def validate(self, data)
    def validate(self, data):
        course_name = data.get('course_name')
        course_duration = data.get('course_duration')
        course = ['bangla', 'ict','english', 'math', 'physics', 'cse', 'eee']
        if course_name.lower() not in course:
            raise serializers.ValidationError('This course are not avabile right now')
        if course_duration > 12:
            raise serializers.ValidationError('Course duration are not allow more then 1 year or 12 mounth')
        return data
    
    # # validotrs
    # from rest_framework import serializers
    # def starts_with_r(value):
    #     if value[0].lower() != 'r':
    #         raise serializers.ValidationError('Name should start with R')
    # class SchoolSerializers(serializers.Serializer):
    #     teacher_name = serializers.CharField(max_length=50, validators=[starts_with_r])
    #     course_name = serializers.CharField(max_length=50) 


# Model serializer
class StudentSerializers(serializers.ModelSerializer):
    # validotrs
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    student_name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = StudentModel
        fields = ['student_name', 'class_name', 'age', 'roll']
        # fields = '__all__'  # Mean all fields in studentModel

    # Field Level Validation : def validate_fieldName(self, value)
    def validate_age(self, value):
        if value > 30:
            raise serializers.ValidationError('Age must less then or equal to 30')
        if value < 10:
            raise serializers.ValidationError('Age must Greater then or equal to 10')
        return value
    
    # Object Level Validation :def validate(self, data)
    def validate(self, data):
        class_name = data.get('class_name')
        roll = data.get('roll')
        c_name = ['six', 'seven','eight', 'nine', 'ten']
        if class_name.lower() not in c_name:
            raise serializers.ValidationError('This class are not avabile right now. Avaible six to ten')
        if roll > 100 or roll < 1:
            raise serializers.ValidationError('Roll are not allow less then 1 or greater then 100')
        return data
    


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

        