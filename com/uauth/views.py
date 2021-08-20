import random
import time
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
# from project.uauth.models import Users
from .models import Users, students, teachers
# from stu.models import StudentInfo
import os
from django.conf import settings

"""def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        return render(request, 'index.html')"""


def index(request):
    is_login = request.COOKIES.get('ticket', False)

    if is_login:
        ticket = request.COOKIES.get('ticket')
        users = Users.objects.get(u_ticket=ticket)
        request.ticket = ticket
        return render(request, 'index.html', {"is_login": 1, "users": users})
    else:
        return render(request, 'index.html', {"is_login": 0})
    # return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        # 注册
        """s_name = request.POST.get('s_name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        Inumber = request.POST.get('Inumber')
        academy = request.POST.get('academy')
        grade = request.POST.get('grade')
        number = request.POST.get('number')
        teacher_name = request.POST.get('teacher_name')
        mail = request.POST.get('mail')"""
        judge = request.POST.get('type')
        if judge == "student":
            s_name = request.POST.get('s_name')
            picture = request.FILES.get('s_picture')
            sex = request.POST.get('s_sex')
            certification_type = request.POST.get('s_certification_type')
            id_number = request.POST.get('s_id_number')
            birthday = request.POST.get('s_birthday')
            politics_status = request.POST.get('s_politics_status')
            college = request.POST.get('s_college')
            grade = request.POST.get('s_grade')
            s_class = request.POST.get('s_class')
            number = request.POST.get('s_number')
            mail = request.POST.get('s_mail')
            phone = request.POST.get('s_phone')
            password = request.POST.get('password')
            password = make_password(password)

            students.objects.create(s_name=s_name, s_picture=picture, s_sex=sex,
                                    s_certification_type=certification_type,
                                    s_id_number=id_number, s_politics_status=politics_status, s_birthday=birthday,
                                    s_college=college, s_grade=grade, s_class=s_class, s_number=number,
                                    s_mail=mail, s_phone=phone, s_password=password)
            Users.objects.create(u_name=s_name, u_phone=phone, u_password=password, u_num=0)

        else:
            t_name = request.POST.get('t_name')
            picture = request.FILES.get('picture')
            sex = request.POST.get('t_sex')
            certification_type = request.POST.get('t_politics_status')
            position = request.POST.get('t_position')
            id_number = request.POST.get('t_id_number')
            birthday = request.POST.get('t_birthday')
            college = request.POST.get('t_college')
            title = request.POST.get('t_title')
            department = request.POST.get('t_department')
            number = request.POST.get('t_number')
            mail = request.POST.get('t_mail')
            phone = request.POST.get('t_phone')
            password = request.POST.get('password')
            password = make_password(password)
            teachers.objects.create(t_name=t_name, t_picture=picture, t_sex=sex,
                                    t_certification_type=certification_type,
                                    t_position=position, t_id_number=id_number, t_birthday=birthday,
                                    t_college=college, t_title=title, t_department=department, t_number=number,
                                    t_mail=mail, t_phone=phone, t_password=password)
            Users.objects.create(u_name=t_name, u_phone=phone, u_password=password, u_num=1)
        # 对密码进行加密
        # password = make_password(password)
        filePath = os.path.join(settings.MEDIA_ROOT, picture.name)
        with open(filePath, 'wb') as fp:
            for info in picture.chunks():
                fp.write(info)
        return HttpResponseRedirect('/')
        # return HttpResponse("注册成功")


"""def signup(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    if request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        Inumber = request.POST.get('Inumber')
        academy = request.POST.get('academy')
        grade = request.POST.get('grade')
        number = request.POST.get('number')
        teacher_name = request.POST.get('teacher_name')
        mail = request.POST.get('mail')
        #对密码进行加密
        password = make_password(password)
        Users.objects.create(u_name=name, u_password=password, u_sex=sex, u_Inumber=Inumber ,u_academy=academy, u_grade=grade, u_number=number,
                             u_teacher_name=teacher_name, u_mail=mail)
        return HttpResponseRedirect('/login/')"""


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if Users.objects.filter(u_phone=name).exists():
            user = Users.objects.get(u_phone=name)
            if check_password(password, user.u_password):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                response = HttpResponse()
                # response = HttpResponseRedirect('/stu/index.html')
                # max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服务端
                user.u_ticket = ticket
                user.save()  # 保存
                return response
                # return HttpResponse("登陆成功")
                # return render(request, 'ui/index.html')
                # return HttpResponseRedirect('/')
                # return render(request, 'index.html')
            else:
                return HttpResponse('用户密码错误')
                # return render(request, "login.html", {"password": "用户密码错误"})
                # return render(request, "login.html", {"msg": u"用户名或者密码错误!"})
        else:
            return HttpResponse('用户不存在')
            # return render(request, 'login.html', {'name': '用户不存在'})


def logout(request):
    if request.method == 'GET':
        # response = HttpResponse()
        response = HttpResponseRedirect('/login/')
        response.delete_cookie('ticket')
        return response


"""def updateinfo(request):
    if request.method == 'POST':
        picture = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        new_img = models.mypicture(
            photo=request.FILES.get('photo'),  # 拿到图片
            user=request.FILES.get('photo').name # 拿到图片的名字
        )
        new_img.save()  # 保存图片
        return HttpResponse('上传成功！')

    return render(request, 'aaa.html')"""
