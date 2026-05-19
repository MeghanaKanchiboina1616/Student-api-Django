from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .Serializers import StudentSerializer
from rest_framework.response import Response
@api_view(['POST'])
def create_stud(request):
    S =StudentSerializer(data=request.data)
    if S.is_valid():
        S.save()
        return Response(S.data)
    return Response(S.errors)

@api_view(['GET'])
def get_stud(request):
    st=Student.objects.all()
    ser=StudentSerializer(st,many=True)
    return Response(ser.data)
