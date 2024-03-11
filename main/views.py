from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import generics
from .models import School
from .models import Summary
from .serializers import SchoolSerializer
from .serializers import SummarySerializer
from .models import Class
from .serializers import ClassSerializer




class SchoolListAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SummaryListAPIView(generics.ListAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    
class ClassListAPIView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
