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
    # UserProfile,
    #UserType,
    AccessToken,
    UserAccount,
    #Class,
    lessons,
    student,
    less_img,
    less_pdf,
    less_aud,
    less_vdo,
    imageByStu,
    pdfByStu,
    audByStu,
    Subject,
    scn,
    
)
from django.contrib.auth.models import User, Group
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserFetchSerializer,
    #ClassSerializer,
    #ClassListSerializer,
    lessonSerializer,
    studentLessonSerializer,
    lessimgSerializer,
    lesspdfSerializer,
    lessaudSerializer,
    lessvdoSerializer,
    lessimgByStuSerializer,
    lesspdfByStuSerializer,
    lessaudByStuSerializer,
    SubjectSerializer,
    scnSerializer,
    revSer
    #reverseSerializer
)
from rest_framework import (
    viewsets,
    permissions,
    generics,
)
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
# filter_backends = (DjangoFilterBackend,)
# filter_fields = ('name','phone','email')
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import filters
from django.core.mail import send_mail
# from CheckoTracker.settings import EMAIL_HOST_USER
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
from django.db import transaction
import logging
logger = logging.getLogger(__name__)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




class UserRegistration(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAccountViewSet(APIView):
    serializer_class = UserFetchSerializer
    def get(self, request, *args, **kwargs):
        data = request.data
        serializer = UserFetchSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        


class UserLoginAPIView(APIView):
    # permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserFetch():
    pass


# @api_view(['POST',])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = "successfully registered new user"
#             data['email'] = account.email
#             data['phone'] = account.phone
#         else:
#             data = serializer.errors
#         return Response(data)


#@api_view(['POST',])
#def Classname(request):

 #   if request.method == 'POST':
  #      serializer = ClassSerializer(data=request.data)
   #     data = {}
    #    if serializer.is_valid():
     #       Class = serializer.save()
      #      data['response'] = "Class Created"
       #     data['class_name'] = Class.class_name
       # else:
        #    data = serializer.errors
       # return Response(data)


#class ClassListView(generics.ListAPIView):
    #serializer_class = ClassListSerializer
    #queryset = Class.objects.all()
    #filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    #filterset_fields = ['id','class_name', 'class_address']
 #   def get(self,request,*args,**kwargs):
  #      qs=Class.objects.all()
   #     serializer=ClassListSerializer(qs,many=True)
    #    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
        #filterset_fields = ['id','class_name', 'class_address']
     #   filter_fields=('class_name',)
      #  return Response(serializer.data)

#class UserClassList(generics.ListAPIView):
 #   def get(self,request,*args,**kwargs):
  #     sq=userClassRelation.objects.all()
   #    serializer=userClassRelationSerializer(sq,many=True)
    #   return Response(serializer.data)


    #pagination_class=None
    #paginate_by = None
    #def get_paginated_response(self, data): 
     #  return Response(data)

class userView(viewsets.ModelViewSet):
    queryset=UserAccount.objects.all()
    serializer_class=UserFetchSerializer
    #pagination_class=None
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response({'status': 'user deleted'})



class screenview(viewsets.ModelViewSet):
	queryset=scn.objects.all()
	serializer_class=scnSerializer
	

            
class LessonListView(viewsets.ModelViewSet):
    queryset = lessons.objects.all()
    serializer_class = lessonSerializer
    #pagination_class=None
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response({'status': 'lesson deleted'})
    #@action(detail=True, methods=['post'])
    #def set_pass(self, request, pk=None):
     #   user = self.get_object()
      #  serializer = lessonSerializer(data=request.data)
       # if serializer.is_valid():
            #user.set_password(serializer.data['password'])
        #    user.save()
         #   return Response({'status': 'lesson created'})
        #else:
         #   return Response(serializer.errors,
#status=status.HTTP_400_BAD_REQUEST)
        

class LessimgView(viewsets.ModelViewSet):
    #permission_classes=(permission.AllowAny,)
    queryset = less_img.objects.all()
    serializer_class = lessimgSerializer
    #pagination_class=None
    #def create(self,request,*args,**kwargs): 
     #   return Response({'image':'created'})

    #def destroy(self,request,*args,**kwargs):
      #  return Response({'image':'deleted'})

class LesspdfView(viewsets.ModelViewSet):
    queryset = less_pdf.objects.all()
    serializer_class = lesspdfSerializer
    #pagination_class=None
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response({'status': 'lesson pdf deleted'})
        #return Response(status=status.HTTP_204_NO_CONTENT)

class LessaudView(viewsets.ModelViewSet):
    queryset = less_aud.objects.all()
    serializer_class = lessaudSerializer
    #pagination_class=None

class LessvdoView(viewsets.ModelViewSet):
    queryset = less_vdo.objects.all()
    serializer_class = lessvdoSerializer
    #pagination_class=None


    

class studentLessonSerializer(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentLessonSerializer
    #pagination_class=None

class LessimgByStu(viewsets.ModelViewSet):
    #permission_classes=(permission.AllowAny,)
    queryset = imageByStu.objects.all()
    serializer_class = lessimgByStuSerializer
    #pagination_class=None
   
class LesspdfByStu(viewsets.ModelViewSet):
    queryset = pdfByStu.objects.all()
    serializer_class = lesspdfByStuSerializer
    #pagination_class=None
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response({'status': 'lesson pdf deleted'})
        #return Response(status=status.HTTP_204_NO_CONTENT)

class LessaudByStu(viewsets.ModelViewSet):
    queryset = audByStu.objects.all()
    serializer_class = lessaudByStuSerializer
    #pagination_class=None

class SubjectView(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    #paginate_by = None
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response({'status': 'subject deleted'})



    #paginator=None
#class UView(viewsets.ModelViewSet):
 #   queryset=UserAccount.objects.all()
  #  serializer_class=reverseSerializer

class revView(viewsets.ModelViewSet):     #testing purpose
    queryset=UserAccount.objects.all()
    serializer_class=revSer

class Testapi(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': ' narottam',
            'email': 'test'
            }
        return Response(data)



