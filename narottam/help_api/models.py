from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, EmailValidator
from django import forms
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
#from core_api.models import lessons

class name(models.Model):                                 #for testing purpose
	s_name=models.CharField(max_length=100)
	#subj_desc=models.CharField(max_length=100)
	#Batch_attached=models.ManyToManyField(Class,blank=True,default=None)
	def __str__(self):
	    return self.s_name

class Class(models.Model):
    #class_name = models.CharField(max_length=200)
	course_name=models.ForeignKey('core_api.Subject',on_delete=models.CASCADE,related_name="subjectadd")
	class_name = models.CharField(max_length=200)
	class_address = models.CharField(max_length = 200)
	time_start=models.TimeField(blank=True,null=True)
	lesson_attached=models.ManyToManyField('core_api.lessons',blank=True, default=None)
	def __str__(self):
            return self.class_name


   
