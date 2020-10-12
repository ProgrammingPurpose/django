from django.contrib.auth import get_user_model
from passlib.hash import pbkdf2_sha256

from .models import (
    name,
    Class,
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


class nameSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=name
		fields=('id','s_name')

class ClassListSerializer(serializers.HyperlinkedModelSerializer):
    #Class = ClassSerializer(many=True)

    class Meta:
        model = Class
        fields = ['id','course_name','class_name', 'class_address','time_start','lesson_attached']

