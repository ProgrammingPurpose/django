from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# import rastframework for API
from rest_framework import viewsets
from rest_framework import status,decorators,parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
# from core_api.serializers import RegistrationSerializer
from django.http import HttpResponse
from .models import (
    name,
    Class
    
)
from django.contrib.auth.models import User, Group
from .serializers import (
    nameSerializer,
    ClassListSerializer
)
# Create your views here.
from rest_framework import (
    viewsets,
    permissions,
    generics,
)

class nview(viewsets.ModelViewSet):
	queryset=name.objects.all()
	serializer_class=nameSerializer


class classView(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassListSerializer
