from rest_framework import serializers
from .models import  Fruit,Task,EducationDetail,Manage,Club,Staff,Student,Course,Module,GenericUser
from phonenumber_field.serializerfields import PhoneNumberField

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = '__all__'

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class GenericUserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = GenericUser
        fields = '__all__' 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['phone_number'] = str(instance.phone_number) 
        return representation
