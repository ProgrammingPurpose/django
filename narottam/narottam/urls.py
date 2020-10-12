"""narottam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core_api import views
from help_api import views as hview
from rest_framework import routers
from core_api.views import( Testapi, UserLoginAPIView, UserRegistration, #Classname, 
UserAccountViewSet,userView,
studentLessonSerializer,
LessonListView,LessimgView,LesspdfView,LessaudView,
LessvdoView,LessaudByStu,LessimgByStu,LesspdfByStu,SubjectView,
screenview,revView)

#from help_api.views import(nview)
router=routers.DefaultRouter()
router.register('api/test',hview.nview)
router.register('api/rev',views.revView)
router.register('api/subject',views.SubjectView)
router.register('api/classes',hview.classView)
router.register('api/users',views.userView)
router.register('api/screen',views.screenview)
router.register('api/lessons',views.LessonListView)
router.register('api/lessImage',views.LessimgView)
router.register('api/lessPdf',views.LesspdfView)
router.register('api/lessAud',views.LessaudView)
router.register('api/lessVdo',views.LessvdoView)
router.register('api/lessons_by_student',views.studentLessonSerializer)
router.register('api/lessImageByStu',views.LessimgByStu)
router.register('api/lessPdfByStu',views.LesspdfByStu)
router.register('api/lessAudByStu',views.LessaudByStu)
#router.register('api/uview',views.UView)
urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('', Testapi.as_view(), name = 'test'),
    path('api/signup/', UserRegistration.as_view(), name = 'signup'),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/users/', UserAccountViewSet.as_view(), name='userfetch'),
    #path('api/addclass/', Classname, name='addclass'),
    #path('api/classlist/', ClassListView.as_view(), name='listclass'),
   # path('api/showclass/',classView, name='classuser'),
    #path('api/showuser/',userView, name='userdt'),






]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
