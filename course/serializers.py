# -*- coding:utf-8 -*-
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from accounts.serializers import TeacherSerializer
from team.models import Team

from .models import Resource, Course, CourseUpdate, TeamUpdate


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        exclude = ('id', 'create_date', 'owner_stu', 'owner_tch')


class CourseSerializer(serializers.ModelSerializer):
    resources_detail = ResourceSerializer(many=True, read_only=True, source='resources')
    teacher_detail = TeacherSerializer(read_only=True, source='teacher')
    assistant_detail = TeacherSerializer(many=True, read_only=True, source='teaching_assistant')

    def create(self, validated_data):
        if Course.objects.filter(title=validated_data.get('title')).exists():
            raise ValidationError('标题重复,创建失败.')
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        if Course.objects.exclude(pk=instance.pk).filter(title=validated_data.get('title')).exists():
            raise ValidationError('标题重复,创建失败.')
        return super().update(instance, validated_data)

    class Meta:
        model = Course
        exclude = ('create_date', 'update_date')


class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('create_date', 'teaching_assistant', 'resources')


class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUpdate
        exclude = ('create_date', 'update_date')


class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamUpdate
        exclude = ('create_date', 'update_date')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('create_date',)
