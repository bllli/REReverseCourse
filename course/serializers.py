# -*- coding:utf-8 -*-
from django.urls import reverse
from django.utils import timezone
from rest_framework import serializers

from rest_framework.exceptions import ValidationError

from .models import Resource, Course


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, course):
        return reverse('course:course-detail', args=[course.id])

    class Meta:
        model = Course
        fields = '__all__'
         # exclude = ('id',)
