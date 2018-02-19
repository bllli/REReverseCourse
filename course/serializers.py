# -*- coding:utf-8 -*-


from django.urls import reverse
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from .models import Resource, Course


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, course: Course) -> str:
        """返回完整url"""
        request = self.context.get('request')
        return request.build_absolute_uri(
            reverse('course:course-detail', args=(course.id,))
        )

    def create(self, validated_data):
        if Course.objects.filter(title=validated_data.get('title')).exists():
            raise ValidationError('标题重复,创建失败.')
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        if Course.objects.exclude(pk=instance.pk).filter(title=validated_data.get('title')).exists():
            raise ValidationError('标题重复,创建失败.')
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        # todo 其他修改字段
        instance.save()
        return instance

    class Meta:
        model = Course
        exclude = ('id', 'create_date', 'update_date')
