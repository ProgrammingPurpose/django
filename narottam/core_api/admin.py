from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import (

    AccessToken,
    UserAccount,
    Class,
    lessons,
    student,
    less_img,
    scn

)
admin.site.register(lessons)
admin.site.register(student)
admin.site.register(less_img)
admin.site.register(scn)
# Register your models here.

@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass
