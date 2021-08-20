from django.shortcuts import render

# Create your views here.
from .models import Race_name, Race_Message, Team, Member
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from uauth.models import Users, students, teachers
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

"""def check_login(fn):
    def wrapper(request,*args,**kwargs):
        if request.COOKIES.get('ticket', False):
            return fn(request,*args,*kwargs)
    return wrapper"""


def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('ticket')  # 拿到设置得cookie
        if not v:
            r = request.path
            # url = '/login/?next='+r
            url = '/login/'
            return HttpResponseRedirect(url)
        return func(request, *args, **kwargs)

    return inner


"""def Check_Login(func):  #自定义登录验证装饰器
    def warpper(request,*args,**kwargs):
        #is_login = request.session.get('IS_LOGIN', False)
        is_login = request.COOKIES.get('ticket', False)
        if is_login:
            func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login")
    return warpper"""


@auth
def apply(request):
    # gradesList = Grades.objects.all()
    Race_nameList = Race_name.objects.all()  # 从数据库获取所有赛事名称
    # race_messageList = Race_Message.object.all()
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    phone = users.u_phone  # 从页面获取登录用户的手机号
    myselfMessage = students.objects.get(s_phone=phone)  # 从数据库获取对应手机号用户的所有信息
    return render(request, 'competitionEntry.html', {"race_names": Race_nameList, "myselfMessage": myselfMessage})


def race_message(request):
    try:
        id = request.GET.get('id')  # 得到页面返回的所选择的赛事名称的id
        obj = Race_Message.objects.filter(m_race=id)  # 从数据库获取对应赛事的所有赛题
        length = len(obj)
        messages = [model_to_dict(_) for _ in obj]
        return JsonResponse({'messages': messages, 'id': 1, 'length': length})  # id为状态值，1为正常 0 为 不正常
    except:
        return JsonResponse({'id': 0})


@auth
def self_message(request):  # 获取个人信息
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    phone = users.u_phone  # 从页面获取登录用户的手机号
    # phone = request.POST.get('phone')
    # i2 = request.POST.get('i2')
    # j = request.POST.get('j')
    # myself_message = students.objects.values().filter(s_phone=phone)
    myself_message = students.objects.get(s_phone=phone)  # 从数据库获取对应手机号用户的所有信息
    # s_name=get_sorted_posts(myself_message)
    # print(myself_message.s_name)
    return JsonResponse({"myself_message": myself_message})


def confirm_self(request):  # 确认个人信息
    s_name = request.POST.get('s_name')
    birthday = request.POST.get('s_birthday')
    college = request.POST.get('s_college')
    grade = request.POST.get('s_grade')
    s_class = request.POST.get('s_class')
    number = request.POST.get('s_number')
    mail = request.POST.get('s_mail')
    phone = request.POST.get('s_phone')
    students.objects.filter(s_phone=phone).update(s_name=s_name)
    students.objects.filter(s_phone=phone).update(s_college=college)
    students.objects.filter(s_phone=phone).update(s_grade=grade)
    students.objects.filter(s_phone=phone).update(s_class=s_class)
    students.objects.filter(s_phone=phone).update(s_number=number)
    students.objects.filter(s_phone=phone).update(s_mail=mail)
    students.objects.filter(s_phone=phone).update(s_birthday=birthday)


@auth
def team(request):  # 填写队伍信息
    try:
        confirm_self(request)  # 首先提交个人信息
        T_phone = request.POST.get('s_phone')  # 队长手机号
        T_message = request.POST.get('T_message')  # 赛事id
        if len(Team.objects.filter(T_phone=T_phone, T_message=T_message)) > 0:
            return JsonResponse({'code': 0, 'msgs': '请勿重复报名！'})  # 报名失败返回0
        T_name = request.POST.get('T_name')  # 队伍名称
        T_slogan = request.POST.get('T_slogan')  # 队伍口号
        T_intro = request.POST.get('T_intro')  # 队伍介绍
        T_leader = request.POST.get('s_name')  # 队长名称
        T_remark = request.POST.get('T_remark')  # 队伍备注
        Team.objects.create(T_name=T_name, T_intro=T_intro, T_slogan=T_slogan, T_leader=T_leader, T_phone=T_phone,
                            T_message=T_message, T_remark=T_remark)
        return JsonResponse({'code': 1})  # 报名成功返回1
    except:
        return JsonResponse({'code': 0, 'msgs': '服务繁忙，请稍后重试！'})  # 报名失败返回0


def addMatchStudent(request):  # 添加比赛队友
    phone = request.GET.get('phone')
    name = request.GET.get('name')
    message_id = request.GET.get('message_id')
    obj = students.objects.filter(s_phone=phone, s_name=name)
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    selfPhone = users.u_phone  # 从页面获取登录用户的手机号
    if selfPhone == phone:
        return JsonResponse({'code': 0, 'msgs': '不能邀请自己'})  # 报名失败返回0
    elif len(Member.objects.filter(member_id=obj[0].id, message_id=message_id)) != 0:
        return JsonResponse({'code': 0, 'msgs': '该用户已存在于队伍中'})  # 报名失败返回0
    elif len(obj) == 0:
        return JsonResponse({'code': 0, 'msgs': '未查询到该用户'})  # 报名失败返回0
    Member.objects.create(message_id=message_id, invite_state=0, member_id=obj[0].id)  # 默认状态为0，等待对方确认
    return JsonResponse({'code': 1, 'msgs': '成功发出邀请，等待对方确认~'})


def deleteMessage(request, id):
    pass