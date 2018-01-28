from django.db import models

from .CONS_TEAM import TEAM_CHOICES, TEAM_CREATING


class Team(models.Model):
    """团队Model"""
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, verbose_name='小组名称')
    status = models.SmallIntegerField(choices=TEAM_CHOICES, default=TEAM_CREATING, verbose_name='团队状态')

    belong = models.ForeignKey('course.Course', null=True, blank=True,
                               verbose_name='本组所属课程', on_delete=models.SET_NULL)
    owner = models.ForeignKey('accounts.Student', null=True, blank=True,
                              related_name='my_groups', verbose_name='组长', on_delete=models.SET_NULL)
    members = models.ManyToManyField('accounts.Student', related_name='added_groups', verbose_name='组员')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ('create_date',)
