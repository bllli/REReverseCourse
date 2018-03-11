from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import LoginForm
from .models import SchoolClass, Teacher, Student
from .serializers import (SchoolClassSerializer, TeacherSerializer, StudentSerializer)
from .permissions import (IsOwnerOrReadOnly, IsTeacherOrCannotCreate)


def login(request):
    """登录"""
    if request.user.is_authenticated:
        messages.warning(request, '用户 {username}, 你已经登陆'.format(username=request.user.username))
        return redirect('index')
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if login_form.is_valid():
            user = login_form.get_and_check_user()
            auth.login(request, user)
            messages.success(request, '欢迎回来, {username}'.format(username=request.user.username))
            return redirect('index')
        else:
            messages.error(request, '账号或密码错误')
    return render(request, 'login.html', {
        'login_form': login_form
    })


@login_required
def logout(request):
    """登出"""
    auth.logout(request)
    messages.success(request, '登出成功, Bye~')
    return redirect('index')


class SchoolClassViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolClassSerializer
    permission_classes = (IsOwnerOrReadOnly, IsTeacherOrCannotCreate)

    def get_queryset(self):
        return SchoolClass.objects.all()


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return Teacher.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return Student.objects.all()
