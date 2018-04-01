from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'course'

router = DefaultRouter()
router.register(r'course', views.CourseViewSet, base_name='course')
router.register(r'resource', views.ResourceViewSet, base_name='resource')
router.register(r'course_update', views.CourseUpdateViewSet, base_name='course_update')
router.register(r'team_update', views.TeamUpdateViewSet, base_name='team_update')
router.register(r'team', views.TeamViewSet, base_name='team')

urlpatterns = [
    url(r'^list/$', views.course_list, name='list-page'),
    url(r'^detail/$', views.course_detail, name='detail-page'),
] + router.urls
