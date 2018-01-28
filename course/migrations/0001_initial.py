# Generated by Django 2.0 on 2018-01-28 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name='课程名称')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('status', models.SmallIntegerField(choices=[(1, '未提交'), (2, '待开始'), (4, '进行中'), (8, '已结束')], default=1, verbose_name='课程状态')),
                ('start_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='课程开始时间')),
                ('finish_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='课程结束时间')),
                ('group_members_min', models.IntegerField(default=1, verbose_name='团队成员下限')),
                ('group_members_max', models.IntegerField(default=20, verbose_name='团队成员上限')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='CourseUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name='课程更新')),
                ('type', models.SmallIntegerField(choices=[(1, '任务'), (2, '通知')], verbose_name='课程更新类型')),
                ('status', models.SmallIntegerField(choices=[(1, '创建中'), (2, '进行中'), (4, '已结束')], default=1, verbose_name='课程更新状态')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('start_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='开始时间')),
                ('finish_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '课程更新',
                'verbose_name_plural': '课程更新',
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='资源名称')),
                ('url', models.URLField(verbose_name='url')),
                ('text', models.TextField(blank=True, null=True, verbose_name='文本')),
                ('type', models.SmallIntegerField(choices=[(1, '文本'), (2, '图片'), (4, '链接'), (8, '文件')], verbose_name='资源类型')),
            ],
            options={
                'verbose_name': '资源',
                'verbose_name_plural': '资源',
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='TeamUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, verbose_name='作业标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('status', models.SmallIntegerField(choices=[(1, '创建中'), (2, '已提交'), (4, '已打回'), (8, '已评价')], default=1, verbose_name='作业状态')),
                ('score', models.SmallIntegerField(blank=True, choices=[(1, '☆'), (2, '☆☆'), (3, '☆☆☆'), (4, '☆☆☆☆'), (5, '☆☆☆☆☆')], null=True)),
                ('score_text', models.TextField(blank=True, null=True, verbose_name='评价内容')),
                ('score_date', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Student', verbose_name='创建者')),
                ('resources', models.ManyToManyField(to='course.Resource', verbose_name='资源')),
                ('scorer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Teacher', verbose_name='评价人')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.CourseUpdate', verbose_name='所属任务')),
            ],
            options={
                'verbose_name': '小组作业',
                'verbose_name_plural': '小组作业',
                'ordering': ('create_date',),
            },
        ),
    ]