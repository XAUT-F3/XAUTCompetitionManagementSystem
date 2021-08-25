# 此文件用于编写关于新闻传入主页面的函数

from admins import models
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from uauth.models import Users


def getFrontNews(request):  # 用于得到前三条新闻数据放在首页
    objs = models.News.objects.all()
    length = objs.count()
    newObjs = [model_to_dict(_) for _ in objs[length - 3:length]]  # 得到最后三条数据并且进行翻转
    newObjs.reverse()
    return JsonResponse({'news': newObjs})


def checkLogin(request):
    is_login = request.COOKIES.get('ticket', False)
    if is_login:
        ticket = request.COOKIES.get('ticket')
        users = Users.objects.get(u_ticket=ticket)
        request.ticket = ticket
        print(users, users.u_name)
        return {"is_login": 1, "users": users}
    else:
        return {"is_login": 0}


def getIndexNews(request):
    return render(request, 'indexNews.html', checkLogin(request))


def getAllNewsLength(request):  # 获取所有新闻长度
    return JsonResponse({'length': models.News.objects.all().count()})


def getOneNews(request):
    return render(request, 'showNews.html')


def getNewsContext(request):
    index = 1
    objects_all = models.News.objects.all()
    print(objects_all.last().context)
    return JsonResponse({'obj': model_to_dict(objects_all.last())})
