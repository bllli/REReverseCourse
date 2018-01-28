from django.db import models
from django.db.models.query import QuerySet

from utils.utils import get_value_in_choices

from .CONS_COURSE import (COURSE_STATUS_CHOICES, COURSE_CREATING,
                          COURSE_UPDATE_CHOICES, COURSE_UPDATE_CREATING,
                          RESOURCE_TYPE_CHOICES, COURSE_UPDATE_TYPE_CHOICES,
                          TEAM_UPDATE_CHOICES, TEAM_UPDATE_CREATING)


class Resource(models.Model):
    """
    资源 分为文本/链接/图片/文件
    """
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True, blank=True, verbose_name='资源名称')
    url = models.URLField(verbose_name='url')
    text = models.TextField(null=True, blank=True, verbose_name='文本')
    type = models.SmallIntegerField(choices=RESOURCE_TYPE_CHOICES, verbose_name='资源类型')

    # 资源既可以被教师上传 也可以被学生上传
    owner_tch = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE, null=True, blank=True)
    owner_stu = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def owner(self):
        return self.owner_stu or self.owner_tch

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '资源'
        verbose_name_plural = verbose_name


class Course(models.Model):
    """
    课程
    """
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200, verbose_name='课程名称')
    content = models.TextField(null=True, blank=True, verbose_name='内容')
    resources = models.ManyToManyField(Resource, verbose_name='资源')
    status = models.SmallIntegerField(choices=COURSE_STATUS_CHOICES, default=COURSE_CREATING, verbose_name='课程状态')

    start_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='课程开始时间')
    finish_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='课程结束时间')
    group_members_min = models.IntegerField(default=1, verbose_name='团队成员下限')
    group_members_max = models.IntegerField(default=20, verbose_name='团队成员上限')

    teacher = models.ForeignKey('accounts.Teacher', null=True, blank=True, verbose_name='负责教师',
                                on_delete=models.SET_NULL, related_name='in_charge_course_set')
    teaching_assistant = models.ManyToManyField('accounts.Teacher', verbose_name='助教', related_name='help_course_set')

    def __str__(self):
        return '{}'.format(self.title)

    def __repr__(self):
        return '课程: {}_{}>'.format(self.title, self.teacher)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    @staticmethod
    def get_public_course_queryset() -> QuerySet:
        return Course.objects.exclude(status=COURSE_CREATING)


class CourseUpdate(models.Model):
    """
    课程更新
    通知: 只是发布一下信息/资料等
    任务: 发布信息资料的同时，要求各个小组提交小组作业
    """
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200, verbose_name='课程更新')
    type = models.SmallIntegerField(choices=COURSE_UPDATE_TYPE_CHOICES, verbose_name='课程更新类型')
    status = models.SmallIntegerField(choices=COURSE_UPDATE_CHOICES, default=COURSE_UPDATE_CREATING,
                                      verbose_name='课程更新状态')
    content = models.TextField(null=True, blank=True, verbose_name='内容')
    resources = models.ManyToManyField(Resource, verbose_name='资源')

    start_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='开始时间')
    finish_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='结束时间')

    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='所属课程')
    creator = models.ForeignKey('accounts.Teacher', null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='创建者')

    @property
    def type_str(self) -> str:
        return get_value_in_choices(COURSE_UPDATE_TYPE_CHOICES, self.type)

    def __str__(self):
        return '{}_{}'.format(self.title, self.type_str)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '课程更新'
        verbose_name_plural = verbose_name


class TeamUpdate(models.Model):
    """
    小组作业 当教师发布一个“任务”类型的课程更新时，每个小组都应提交自己小组的小组作业
    """
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200, verbose_name='作业标题')
    content = models.TextField(null=True, blank=True, verbose_name='内容')
    resources = models.ManyToManyField(Resource, verbose_name='资源')
    status = models.SmallIntegerField(choices=TEAM_UPDATE_CHOICES, default=TEAM_UPDATE_CREATING,
                                      verbose_name='作业状态')

    task = models.ForeignKey(CourseUpdate, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='所属任务')
    team = models.ForeignKey('team.Team', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='所属小组')
    creator = models.ForeignKey('accounts.Student', null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='创建者')

    score = models.SmallIntegerField(choices=(
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆'),
    ), null=True, blank=True)
    score_text = models.TextField(null=True, blank=True, verbose_name='评价内容')
    score_date = models.DateTimeField(null=True, blank=True)
    scorer = models.ForeignKey('accounts.Teacher', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='评价人')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '小组作业'
        verbose_name_plural = verbose_name
