from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from uauth.models import students, teachers
from apply.models import Team
import csv
import codecs
import time


# ######  后台
def admins(request):
    return render(request, 'admin.html')


def studentdata(request):
    name = '学生数据'
    page_num = request.GET.get('page', 1)
    data = students.objects.all()
    # all_data = [b.s_name,b.s_sex,b.s_birthday,b.s_class,b.s_college,b.s_number,b.s_mail]
    # 初始化page函数  2表示每页信息数
    paginator = Paginator(data, 3)
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())


def studentdatacsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename = "studentdata.csv"'
    response.write(codecs.BOM_UTF8)
    data = students.objects.all()
    writer = csv.writer(response)
    writer.writerow(['名字', '性别', '生日', '班级', '学院', '学号', '邮箱', '身份证件号', '手机号'])
    for b in data:
        writer.writerow(
            [b.s_name, b.s_sex, b.s_birthday, b.s_class, b.s_college, b.s_number, b.s_mail, b.s_phone, b.s_id_number])
    return response


def teacherdata(request):
    name = '老师数据'
    page_num = request.GET.get('page', 1)
    data = teachers.objects.all()
    # 初始化page函数  2表示每页信息数
    paginator = Paginator(data, 3)
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())


def teacherdatacsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename = "teacherdata.csv"'
    response.write(codecs.BOM_UTF8)
    data = teachers.objects.all()
    writer = csv.writer(response)
    writer.writerow(['名字', '性别', '生日', '所在系', '学院', '教职工号', '邮箱', '身份证件号', '手机号'])
    for b in data:
        writer.writerow([b.t_name, b.t_sex, b.t_birthday, b.t_department, b.t_college, b.t_number, b.t_mail, b.t_phone,
                         b.t_id_number])
    return response


def teamdata(request):
    name = '队伍数据'
    page_num = request.GET.get('page', 1)
    data = Team.objects.all()
    # 初始化page函数  2表示每页信息数
    paginator = Paginator(data, 3)
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())


def teamdatacsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename = "teamdata.csv"'
    response.write(codecs.BOM_UTF8)
    data = Team.objects.all()
    writer = csv.writer(response)
    writer.writerow(['团队名称', '团队介绍', '团队备注', '队长名称', '队长手机号', '赛事状态', '获奖情况'])
    for b in data:
        writer.writerow([b.T_name, b.T_intro, b.T_remark, b.T_leader, b.T_phone, b.T_state, b.T_honor])
    return response
