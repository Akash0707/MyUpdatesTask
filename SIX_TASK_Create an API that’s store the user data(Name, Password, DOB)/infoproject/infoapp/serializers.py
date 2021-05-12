from rest_framework import serializers
from .models import Student
import datetime

class StudentSerializer(serializers.Serializer):
 name= serializers.CharField(max_length=100)
 password = serializers.CharField()
 #date=serializers.DateField(initial=datetime.date.today)
 date = serializers.DateField()

 def create(self, validated_data):
  return Student.objects.create(**validated_data)