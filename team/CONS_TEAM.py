TEAM_CREATING = 0x01
TEAM_CREATED = 0x02
TEAM_LOCKED = 0x04

TEAM_CHOICES = (
    (TEAM_CREATING, '创建中'),  # 团队创建中
    (TEAM_CREATED, '已完成'),  # 团队组建完成，拒绝其他用户申请加入
    (TEAM_LOCKED, '已锁定'),  # 课程开始后禁止修改成员
)
