from django.shortcuts import render
from rest_framework import viewsets
from students.models import Student
from students.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):  # já temos modelo vinculado, por isso usar o ModelViewSet
    queryset = Student.objects.all()  # indicará o queryset que utilizaremos
    serializer_class = StudentSerializer  # classe responsavel por serializar


