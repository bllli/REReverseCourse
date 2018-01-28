from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from utils.utils import get_value_in_choices

from .CONS_MESSAGE import MESSAGE_TYPE_CHOICES, MESSAGE_STATUS_CREATING, MESSAGE_STATUS_CHOICES


class Message(models.Model):
    create_date = models.DateTimeField(auto_now=True)

    type = models.SmallIntegerField(choices=MESSAGE_TYPE_CHOICES, verbose_name='站内信类型')
    status = models.SmallIntegerField(choices=MESSAGE_STATUS_CHOICES, default=MESSAGE_STATUS_CREATING,
                                      verbose_name='站内信状态')

    # 发起者(学生/教师)
    actor_content_type = models.ForeignKey(ContentType, related_name='message_actor', on_delete=models.CASCADE)
    actor_object_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    # 发给谁(学生/教师)
    target_content_type = models.ForeignKey(ContentType, related_name='message_target', blank=True, null=True,
                                            on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    # refer 提到了哪个课程/任务/作业/小组
    refer_content_type = models.ForeignKey(ContentType, related_name='message_refer', blank=True, null=True,
                                           on_delete=models.CASCADE)
    refer_object_id = models.PositiveIntegerField(blank=True, null=True)
    refer = GenericForeignKey('refer_content_type', 'refer_object_id')

    content = models.TextField(null=True, blank=True, verbose_name='内容')

    @property
    def type_str(self):
        return get_value_in_choices(MESSAGE_TYPE_CHOICES, self.type)

    @property
    def status_str(self):
        return get_value_in_choices(MESSAGE_STATUS_CHOICES, self.status)

    def __str__(self):
        return 'Message: {}_{}_{}'.format(self.type_str, self.status_str, self.content)

    class Meta:
        ordering = ('create_date',)
        verbose_name = '站内信'
        verbose_name_plural = verbose_name
