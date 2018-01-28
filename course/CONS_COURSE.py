# 课程
COURSE_CREATING = 0x01  # 课程创建中。还是草稿，尚未发布。仅创建者可以查看到。
COURSE_HOLDING = 0x02  # 已创建完成，公布给指定班级。允许学生在本课程中自由结组。
COURSE_STARTED = 0x04  # 已开始。此时分组不可变更，未组队的学生将自动结组。
COURSE_FINISHED = 0x08  # 已结束。此时应拒绝非管理员的修改操作。

COURSE_STATUS_CHOICES = (
    (COURSE_CREATING, '未提交'),  # 课程尚未提交。除提交教师本人外不可查看
    (COURSE_HOLDING, '待开始'),  # 课程已提交，但尚未开始。学生此时组队
    (COURSE_STARTED, '进行中'),  # 课程已经开启。
    (COURSE_FINISHED, '已结束'),  # 课程已经结束。统计，出结果、出成绩
)

# 课程更新状态
COURSE_UPDATE_CREATING = 0x01
COURSE_UPDATE_STARTED = 0x02
COURSE_UPDATE_FINISHED = 0x04

COURSE_UPDATE_CHOICES = (
    (COURSE_UPDATE_CREATING, '创建中'),
    (COURSE_UPDATE_STARTED, '进行中'),
    (COURSE_UPDATE_FINISHED, '已结束'),
)

# 课程更新类型
COURSE_UPDATE_TYPE_TASK = 0x01
COURSE_UPDATE_TYPE_POST = 0x02

COURSE_UPDATE_TYPE_CHOICES = (
    (COURSE_UPDATE_TYPE_TASK, '任务'),  # 本次课程更新是一项任务，需要各小组提交文章
    (COURSE_UPDATE_TYPE_POST, '通知'),  # 本次课程更新只是一个通知，不需要各小组提交文章
)

# 资源类型
RESOURCE_TYPE_TEXT = 0x01
RESOURCE_TYPE_IMG = 0x02
RESOURCE_TYPE_WEB = 0x04
RESOURCE_TYPE_FILE = 0x08

RESOURCE_TYPE_CHOICES = (
    (RESOURCE_TYPE_TEXT, '文本'),
    (RESOURCE_TYPE_IMG, '图片'),
    (RESOURCE_TYPE_WEB, '链接'),
    (RESOURCE_TYPE_FILE, '文件'),
)

# 小队作业状态
TEAM_UPDATE_CREATING = 0x01
TEAM_UPDATE_SUBMITTED = 0x02
TEAM_UPDATE_REJECTED = 0x04
TEAM_UPDATE_SCORED = 0x08

TEAM_UPDATE_CHOICES = (
    (TEAM_UPDATE_CREATING, '创建中'),
    (TEAM_UPDATE_SUBMITTED, '已提交'),
    (TEAM_UPDATE_REJECTED, '已打回'),
    (TEAM_UPDATE_SCORED, '已评价'),
)
