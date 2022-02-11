# 此文件用于编写关于新闻传入主页面的函数

from admins import models
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from admins.views import getNewsList
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
        return {"is_login": 1, "users": users}
    else:
        return {"is_login": 0}


def getIndexNews(request):
    data = checkLogin(request)
    data['count'] = models.News.objects.all().count()
    return render(request, 'indexNews.html', data)


def getAllNewsLength(request):  # 获取所有新闻长度
    return JsonResponse({'length': models.News.objects.all().count()})


def getIndexNewsDetails(request):  # 获取所有新闻不同页面数据
    page = int(request.GET.get('page'))  # 页码数
    limit = int(request.GET.get('limit'))  # 想获取的新闻条数
    length = models.News.objects.all().count()

    if page * limit > length:  # 如果超过总需求
        data = [model_to_dict(_) for _ in models.News.objects.all()[0: length - (page - 1) * limit]]
    else:
        data = [model_to_dict(_) for _ in models.News.objects.all()[length - page * limit: length - (page - 1) * limit]]
    data.reverse()
    return JsonResponse({'data': data, 'length': length, 'trueLength': len(data)})


def getOneNews(request, id):
    news = models.News.objects.get(id=id)
    length = models.News.objects.count()
    if id > 3:
        data = [{'title': _.title, 'id': _.id} for _ in models.News.objects.all()[length - 3: length]]
    else:
        data = [{'title': models.News.objects.get(id=id - _).title, 'id': news.id - _} for _ in range(1, id)]
    return render(request, 'newsDetail.html', {'news': news, 'data': data})
