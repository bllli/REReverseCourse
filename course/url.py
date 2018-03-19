from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'course'

router = DefaultRouter()
router.register(r'course', views.CourseViewSet, base_name='course')
router.register(r'resource', views.ResourceViewSet, base_name='resource')

urlpatterns = [
    url(r'^list/$', views.course_list, name='list-page'),
    url(r'^detail/$', views.course_detail, name='detail-page'),
] + router.urls
