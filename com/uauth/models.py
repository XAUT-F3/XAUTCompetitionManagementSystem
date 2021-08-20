from django.db import models


class Users(models.Model):
    u_name = models.CharField(max_length=30)
    u_phone = models.CharField(max_length=20)
    u_password = models.CharField(max_length=255)
    u_num = models.IntegerField()
    u_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'users'


class students(models.Model):
    s_name = models.CharField(max_length=30, null=True)  # 姓名
    s_picture = models.ImageField(max_length=255, null=True)  # 图片
    s_sex = models.CharField(max_length=10, null=True)  # 性别
    s_certification_type = models.CharField(max_length=20, null=True)  # 身份证件类型
    s_id_number = models.CharField(max_length=30, null=True)  # 身份证件号
    s_birthday = models.DateTimeField(blank=True, null=True)  # 出生日期
    s_politics_status = models.CharField(max_length=30, null=True)  # 政治面貌
    s_college = models.CharField(max_length=20, null=True)  # 学院
    s_grade = models.CharField(max_length=20, null=True)  # 年级
    s_class = models.CharField(max_length=20, null=True)  # 班级
    s_number = models.CharField(max_length=20, null=True)  # 学号
    s_mail = models.CharField(max_length=30, null=True)  # 电子邮箱
    s_phone = models.CharField(max_length=20, null=True)  # 电话号码
    s_password = models.CharField(max_length=255, null=True)  # 密码

    class Meta:
        db_table = 'students'


class teachers(models.Model):
    t_name = models.CharField(max_length=30, null=True)  # 姓名
    t_picture = models.ImageField(max_length=255, null=True)  # 图片
    t_sex = models.CharField(max_length=10, null=True)  # 性别
    t_certification_type = models.CharField(max_length=20, null=True)  # 身份证件类型
    t_id_number = models.CharField(max_length=30, null=True)  # 身份证件号
    t_birthday = models.DateTimeField(blank=True, null=True)  # 出生日期
    t_position = models.CharField(max_length=20, null=True)  # 行政职务
    t_college = models.CharField(max_length=20, null=True)  # 学院
    t_title = models.CharField(max_length=20, null=True)  # 职称
    t_department = models.CharField(max_length=20, null=True)  # 所在系
    t_number = models.CharField(max_length=20, null=True)  # 教职工号
    t_mail = models.CharField(max_length=30, null=True)  # 电子邮箱
    t_phone = models.CharField(max_length=20, null=True)  # 电话号码
    t_password = models.CharField(max_length=255, null=True)  # 密码

    class Meta:
        db_table = 'teachers'
