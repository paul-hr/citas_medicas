from django.shortcuts import render

# Create your views here.
from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# GET /api/Doctors => Listar
# POST /api/Doctors => Crear
# GET /api/Doctors/<pk>/ => Detalle
# PUT /api/Doctors/<pk>/ => Modificación
# DELETE /api/Doctors/<pk>/ => Borrar


class ListDoctorsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()