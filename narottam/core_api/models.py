#from symtable import Class

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, EmailValidator
from django import forms

User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
from help_api.models import name,Class
validEmail = EmailValidator()

# Create your models here.

class AccessToken(models.Model):
    # accessTokenId = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=10)
    access_token = models.CharField(max_length=64)
    createdAt = models.DateTimeField(auto_now_add=True)



class UserAccount(models.Model):
    # retailer_id = models.AutoField(primary_key=True)
    #class_name=models.ForeignKey('Class',on_delete=models.CASCADE,
#related_name="class_assigned")
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, validators=[validEmail])
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=20, default='student')
    address = models.CharField(max_length=250)
    class_enrolled = models.ManyToManyField(Class,blank=True, default=None, related_name="enrolledClasses")

    def __str__(self):
        return self.fullname

class less_img(models.Model):
	#imna=models.CharField(max_length=10,blank=True)
	image_name=models.CharField(max_length=50,blank=True)
	image=models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
	def __str__(self):
	    return self.image_name
	
class less_pdf(models.Model):
	pdf_name=models.CharField(max_length=50,blank=True)
	pdf=models.FileField(upload_to='Doc/',default='Doc/None/No-pdf.pdf')

class less_aud(models.Model):
	aud_name=models.CharField(max_length=50,blank=True)
	aud=models.FileField(upload_to='Audio/',default='Audio/None/No-audio.3gp')

class less_vdo(models.Model):
	vdo_name=models.CharField(max_length=50,blank=True)
	vdo=models.FileField(upload_to='Video/',default='Video/None/No-video.mp4')


class scn(models.Model):
	Scn_name = models.CharField(max_length=30)
	Scn_desc = models.CharField(max_length=30)
	image=models.ImageField(upload_to='images/',
default='images/None/No-img.jpg')
	pdf=models.FileField(upload_to='pdfs/',default='pdfs/None/No-pdf.pdf')
	audio=models.FileField(upload_to='ados/',default='ados/None/No-pdf.3gp')
	video=models.FileField(upload_to='videos/',
default='videos/None/No-pdf.mp4')
	def __str__(self):
	    return self.Scn_name

class lessons(models.Model):                               #post
	#id_pr=models.CharField(max_length=10)
	#id_pr=models.ForeignKey(Practise)
	lesson_name=models.CharField(max_length=30)
	data=models.CharField(max_length=30)
	#imgAttached=models.ManyToManyField(less_img,blank=True,
#default=None)
	#pdf_attached=models.ManyToManyField(less_pdf,blank=True,
#default=None)
	#aud_attached=models.ManyToManyField(less_aud,blank=True,
#default=None)
	#vdo_attached=models.ManyToManyField(less_vdo,blank=True,
#default=None)
	screen = models.ManyToManyField(scn,related_name='cd')
	student_enrolled=models.ManyToManyField(UserAccount,
blank=True,default=None,related_name='entry')	
	nm = models.ManyToManyField(name,related_name='c')   #testing
	def __str__(self):
	    return self.lesson_name


 #student_enrolled=models.ManyToManyField(UserAccount,blank=True,default=None)
    
    

class Subject(models.Model):
	subject_name=models.CharField(max_length=100)
	#subj_desc=models.CharField(max_length=100)
	#Batch_attached=models.ManyToManyField(Class,blank=True,default=None)
	def __str__(self):
	    return self.subject_name




class imageByStu(models.Model):
	image_stu=models.ImageField(upload_to='Student_Images_lesson/',default='Images/None/No-img.jpg')

class pdfByStu(models.Model):
	pdf_stu=models.FileField(upload_to='student_Doc/',default='Doc/None/No-pdf.pdf')

class audByStu(models.Model):
	aud_stu=models.FileField(upload_to='student_Audio/',default='Audio/None/No-audio.3gp')


class student(models.Model):
	lessonName=models.CharField(max_length=30)
	text_lesson=models.CharField(max_length=30)
	imgAttachedByStu=models.ManyToManyField(imageByStu,blank=True,
default=None)
	pdf_attachedByStu=models.ManyToManyField(pdfByStu,blank=True,
default=None)
	aud_attachedByStu=models.ManyToManyField(audByStu,blank=True,
default=None)
	
	submitted_by=models.CharField(max_length=30)
	def __str__(self):
	    return self.submitted_by





	
    #@property
    #def class_assigned(self):
     #   return self.UserAccount.class_name
