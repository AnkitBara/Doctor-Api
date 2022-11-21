from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import doctors
from .serializers import doctorsSerializer


# Create your views here.

class doctersList(APIView):
    def get(self,request):
        doctor = doctors.objects.all()
        serializer = doctorsSerializer(doctor, many = True)
        return Response(serializer.data)



    def post(self):
        pass

