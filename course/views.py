from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
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


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CourseList(APIView):
    """教学负责人新增/多个红米5plus查询API"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get_query(self):
        return Course.objects.all()

    def get(self, request, format=None) -> Response:
        query = self.get_query()
        data = CourseSerializer(query, many=True, context={'request': request}).data
        return Response({
            'data': data
        }, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """创建新课程"""
        serializer = CourseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'data': serializer.errors, 'msg': '创建失败',
            }, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @staticmethod
    def get_object(course_id: int) -> Course:
        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise Http404({
                'msg': '404 NOT FOUND',
            })

    def get(self, request, course_id: int, format=None) -> Response:
        """获取某个课程"""
        course = self.get_object(course_id)
        serializer = CourseSerializer(course, context={'request': request})
        return Response({
            'data': serializer.data, 'msg': '200 OK'
        }, status=status.HTTP_200_OK)

    def put(self, request, course_id: int, format=None) -> Response:
        """修改某课程"""
        course = self.get_object(course_id)
        serializer = CourseSerializer(course, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
            }, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'data': serializer.errors, 'msg': '400 BAD REQUEST',
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id: int, format=None) -> Response:
        """删除某课程"""
        course = self.get_object(course_id)
        if course:
            course.delete()
            return Response({'msg': '删除成功'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'msg': '未找到要删除的课程'}, status=status.HTTP_404_NOT_FOUND)
