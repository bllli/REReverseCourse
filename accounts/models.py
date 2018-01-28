from django.contrib.auth.models import User
from django.db import models

from .helper import get_sentinel_user


class SchoolClass(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='班级名称')
    head_teacher = models.ForeignKey('Teacher',
                                     on_delete=models.SET_NULL,
                                     default=None, null=True, blank=True,
                                     verbose_name='班主任')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '班级信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """教师Model"""
    create_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.SET(get_sentinel_user))
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='教师姓名')
    tch_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='教工号')
    banned = models.BooleanField(default=False, verbose_name='是否停用')

    class Meta:
        ordering = ('create_date',)
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name


class Student(models.Model):
    """学位Model"""
    create_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.SET(get_sentinel_user))
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='学生姓名')
    stu_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='学号')
    banned = models.BooleanField(default=False, verbose_name='是否停用')

    school_classes = models.ManyToManyField(SchoolClass)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def in_class(self, school_class: SchoolClass) -> bool:
        """检测用户是否处于班级内"""
        return True if self in school_class.student_set else False
