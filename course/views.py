from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer


def course_list(request):
    return render(request, 'course/list.html', {
    })


def course_detail(request, course_id: int):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/detail.html', {
    })


class CourseList(APIView):
    """教学负责人新增/多个查询API"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_query(self):
        return Course.objects.all()

    def get(self, request, format=None):
        query = self.get_query()
        data = CourseSerializer(query, many=True, context={'request': request}).data
        return Response({'status': status.HTTP_200_OK, 'result': {
            'data': data
        }})


class CourseDetail(APIView):
    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404({
                "status": status.HTTP_404_NOT_FOUND, "data": "", "msg": ""
            })

    def get(self, request, id, format=None):
        course = self.get_object(id=id)
        serializer = CourseSerializer(course, context={'request': request})
        return Response({
            "status": status.HTTP_200_OK,
            "data": serializer.data,
            "msg": "ok"
        })

    def put(self, request, id, format=None):
        return Response({
            "status": status.HTTP_202_ACCEPTED,
            "data": "",
            "msg": ''
        })
