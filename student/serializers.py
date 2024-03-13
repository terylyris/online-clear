from rest_framework import serializers
from models import School,Department,Course,Student,UnitsDone,Results

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UnitsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsDone
        fields = "__all__"

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"