from django.db import models

# Create your models here.

"""class Users(models.Model):

    u_phone = models.CharField(max_length=20)
    u_password = models.CharField(max_length=255)
    u_num = models.IntegerField()
    u_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'users'"""


class Race_name(models.Model):
    r_name = models.CharField(max_length=30)  # 赛事名称

    class Meta:
        db_table = 'race_name'


class Race_Message(models.Model):
    m_name = models.CharField(max_length=30)  # 赛题名称
    m_content = models.TextField(null=True)  # 赛题内容
    m_signup_requset = models.TextField(null=True)  # 报名要求
    m_work_request = models.TextField(null=True)  # 作品要求
    m_race = models.IntegerField()

    # m_race = models.ForeignKey("Race_name", on_delete=models.CASCADE)#关联外键
    class Meta:
        db_table = 'race_message'


class Team(models.Model):
    T_name = models.CharField(max_length=30)  # 团队名称
    T_slogan = models.TextField()  # 团队口号
    T_intro = models.TextField()  # 团队介绍
    T_remark = models.TextField(null=True)  # 团队备注
    T_leader = models.CharField(max_length=10)  # 队长名称
    T_phone = models.CharField(max_length=20)  # 队长手机号
    T_state = models.CharField(max_length=20, null=True)  # 赛事状态
    T_honor = models.CharField(max_length=20, null=True)  # 获奖情况
    T_message = models.IntegerField()

    # T_message = models.ForeignKey("Race_Message", on_delete=models.CASCADE)#关联外键
    class Meta:
        db_table = 'team'


class Member(models.Model):
    message_id = models.IntegerField()  # 赛事id
    member_id = models.IntegerField()  # 成员id
    invite_state = models.IntegerField()  # 邀请状态，0为邀请中，1为已邀请成功

    class Meta:
        db_table = 'member'
