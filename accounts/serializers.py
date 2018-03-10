# -*- coding:utf-8 -*-
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers, status

from .models import Student, Teacher, SchoolClass


class DateTimeTzAwareField(serializers.DateTimeField):
    def to_representation(self, value):
        if value:
            value = timezone.localtime(value)
        return super().to_representation(value)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('user', 'create_date')

    def create(self, validated_data):
        user = User.objects.get_or_create(username='tch{}'.format(
            validated_data['tch_id']
        ))[0]
        return Teacher.objects.update_or_create(
            user=user, defaults={
                'name': validated_data['name'],
                'tch_id': validated_data['tch_id'],
                'banned': validated_data['banned'],
            }
        )[0]


class SchoolClassSerializer(serializers.ModelSerializer):
    create_date = DateTimeTzAwareField(format='%Y-%m-%d %H:%S', read_only=True)
    head_teacher_detail = TeacherSerializer(source='head_teacher', read_only=True)

    class Meta:
        model = SchoolClass
        # exclude = ('create_date', )
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    school_classes_detail = SchoolClassSerializer(read_only=True, many=True, source='school_classes')

    class Meta:
        model = Student
        exclude = ('user', 'create_date')

    def create(self, validated_data):
        user = User.objects.get_or_create(username='stu{}'.format(
            validated_data['stu_id']
        ))[0]
        stu = Student.objects.update_or_create(
            user=user, defaults={
                'name': validated_data['name'],
                'stu_id': validated_data['stu_id'],
                'banned': validated_data['banned'],
            }
        )[0]
        stu.school_classes.clear()
        for c in validated_data['school_classes']:
            stu.school_classes.add(c)
        stu.save()
        return stu
