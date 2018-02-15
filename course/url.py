from django.conf.urls import url

from . import views

app_name = 'course'

urlpatterns = [
    url(r'^list/$', views.course_list, name='list-page'),
    url(r'^detail/$', views.course_detail, name='detail-page'),
    url(r'^$', views.CourseList.as_view(), name='course-list'),
    url(r'^(?P<id>[0-9]+)/$', views.CourseDetail.as_view(), name='course-detail'),
]
