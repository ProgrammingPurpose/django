from django.contrib.auth import get_user_model
from passlib.hash import pbkdf2_sha256

from .models import (
    # UserProfile,
    # UserType,
    AccessToken,
    # Account,
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
#from .models import *
from rest_framework import serializers
import logging
logger = logging.getLogger(__name__)
User = get_user_model()
from rest_framework.serializers import (
    CharField,
    EmailField,
    # HyperlinkedIndetityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
import random
import string




def get_random_alphaNumeric_string(stringLength=32):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    phone = CharField(required=True)
    user_id = CharField(allow_blank=True, read_only=True)
    # usertype = CharField(allow_blank=True, read_only=True)
    # email = EmailField(label='Email Address', required=False, allow_blank=True)
    class Meta:
        model = UserAccount
        fields = [
            'phone',
            'password',
            'token',
            'user_id',
            'usertype',
        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                        }


    def validate(self, data):
        # username = data.get("username", None)
        phone = data.get("phone", None)
        raw_password = data.get('password', None)
        if not phone and not raw_password:
            raise ValidationError("Phone Number and password is required")
        retailer = UserAccount.objects.filter(phone=phone)
        access_token = AccessToken.objects.filter(phone=phone)
        if len(retailer) == 0:
            raise ValidationError("Phone Number is not registered")
        elif len(retailer) == 1:
            if pbkdf2_sha256.verify(raw_password, retailer[0].password):
                data["token"] = access_token[0].access_token
                data["user_id"] = retailer[0].id
                data["usertype"] = retailer[0].usertype
                return data
            else:
                raise ValidationError("Incorrect credentials. Please try again")
        else:
            raise ValidationError("Multiple User with same Phone Number")





class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # usertype = serializers.ReadOnlyField(source="usertype_id.usertype")
    # company_name = serializers.ReadOnlyField(source="company_id.company_name")
    class Meta:
        model = UserAccount
        fields = ['fullname', 'password', 'password2', 'email', 'phone', 'address', 'usertype']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def create(self, validated_data):
        print("-----------------{}----------".format(validated_data))

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        phone = self.validated_data['phone']
        queryset = UserAccount.objects.filter(phone=phone)
        if queryset:
            raise serializers.ValidationError({'phone': 'This Phone number already exist'})
        if password != password2:
            raise serializers.ValidationError({'password': 'Password Must Match'})
        # retailer.set_password(password)
        enc_password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32)
        validated_data['password'] = enc_password
        validated_data.pop('password2')
        retailer = UserAccount.objects.create(**validated_data)
        retailer.save()
        AccessToken.objects.create(phone=phone, access_token=get_random_alphaNumeric_string(32))
        return retailer

#class ClassSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Class
   #     fields = ['class_name', 'class_address']



class UserFetchSerializer(serializers.HyperlinkedModelSerializer):
    #products = serializers.SerializerMethodField()
    # users = serializers.StringRelatedField(many=True)
    # print(users)
    #class_name=serializers.RelatedField(source='UserAccount',read_only=True)
    #class_name=serializers.CharField(source="class_name.class_name",read_only=True)
    class Meta:
        model = UserAccount
        fields = ('id','fullname', 'email', 'phone','class_enrolled')
        #fields="__all__"
        #def get_name(self,obj):
         #   return obj.class_name.class_name
        


class scnSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model=scn
		fields=('id','Scn_name','Scn_desc','image',
'pdf','audio','video')


class lessonSerializer(serializers.HyperlinkedModelSerializer):
	
	
	class Meta:
		model=lessons
		fields=('id','lesson_name','data',
'screen','nm')

class lessimgSerializer(serializers.ModelSerializer):
	image=serializers.ImageField(max_length=None,use_url=True)
	class Meta:
		model=less_img
		fields=('id','image_name','image')

class lesspdfSerializer(serializers.HyperlinkedModelSerializer):
	pdf=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=less_pdf
		fields=('id','pdf_name','pdf')

class lessaudSerializer(serializers.HyperlinkedModelSerializer):
	aud=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=less_aud
		fields=('id','aud_name','aud')

class lessvdoSerializer(serializers.HyperlinkedModelSerializer):
	vdo=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=less_vdo
		fields=('id','vdo_name','vdo')
	
       
class studentLessonSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model=student
		fields=('lessonName','text_lesson','imgAttachedByStu','pdf_attachedByStu','aud_attachedByStu','submitted_by')

	
	

class lessimgByStuSerializer(serializers.HyperlinkedModelSerializer):
	image_stu=serializers.ImageField(max_length=None,use_url=True)
	class Meta:
		model=imageByStu
		fields=('id','image_stu')

class lesspdfByStuSerializer(serializers.HyperlinkedModelSerializer):
	pdf_stu=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=pdfByStu
		fields=('id','pdf_stu')

class lessaudByStuSerializer(serializers.HyperlinkedModelSerializer):
	aud_stu=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=audByStu
		fields=('id','aud_stu')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Subject
		fields=('id','subject_name')





class revSer(serializers.ModelSerializer):
	details=serializers.SerializerMethodField()
	class Meta:
		model=UserAccount
		fields=('id','fullname','details')
	def get_details(self,obj):
		details=obj.entry.all()
		response=lessonSerializer(details,
many=True).data
		return response




	












