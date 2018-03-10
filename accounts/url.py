from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'accounts'

router = DefaultRouter()
router.register(r'class', views.SchoolClassViewSet, base_name='class')
router.register(r'tch', views.TeacherViewSet, base_name='tch')
router.register(r'stu', views.StudentViewSet, base_name='stu')

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
] + router.urls
