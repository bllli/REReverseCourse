from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from accounts.permissions import IsOwnerOrReadOnly, IsTeacherOrCannotCreate

from . import CONS_COURSE
from .models import Course, Resource
from .serializers import CourseSerializer, ResourceSerializer


def course_list(request):
    return render(request, 'course/list.html')


def course_detail(request, course_id: int):
    get_object_or_404(Course, course_id)
    return render(request, 'course/detail.html', {
        'course_id': course_id,
    })


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return Resource.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (IsOwnerOrReadOnly, IsTeacherOrCannotCreate)

    def get_queryset(self):
        return Course.objects.exclude(status=CONS_COURSE.COURSE_CREATING).all()

    def list(self, request, *args, **kwargs):
        if request.GET.get('myself', None) and request.user.is_authenticated:
            print(request.user.id)
            self.queryset = Course.objects.filter(teacher__user=request.user).all()
        tch_id = request.GET.get('tch_id')
        if tch_id:
            self.queryset = Course.objects.filter(teacher__tch_id=tch_id).all()
        return Response(self.serializer_class(self.queryset, many=True).data)
