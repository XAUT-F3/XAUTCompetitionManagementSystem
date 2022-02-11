import random

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from com import settings


def random_str():
    _str = '1234567890abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(_str) for i in range(4))


def send_email(request):
    """
    邮件发送函数。ajax发送get请求，调用随机字符串函数，生成四位随机数，保存到session中，
    并发送邮件到验证邮箱。
    post请求中判断得到的随机字符串是否与session中所保存的字符串相同，若相同则重定向到主页面。
    """
    if request.method == 'GET':
        try:
            email = request.GET['email']
        except:
            email = ''
        email_code = random_str()
        msg = '您好，你的验证码为： ' + email_code + '  请与5分钟内使用，过期无效。'
        send_mail('【西安理工大学】邮箱验证', msg, settings.EMAIL_FROM,
                  [email])
        # 将验证码保存到session中在接下来的操作中进行验证
        request.session['email_code'] = email_code
        return JsonResponse({'code': 1})  # 1表示发送验证码成功
    else:
        # 验证验证码是否输入正确
        if request.POST.get('email_code') == request.session['email_code']:
            return True
        else:
            return False


def checkCode(request):
    # 验证验证码是否输入正确
    if request.GET.get('email_code') == request.session['email_code']:
        print(request.GET.get('email_code'))
        return JsonResponse({'code': 1})  # 如果验证成功
    else:
        return JsonResponse({'code': 0})
