from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from . import models


# Create your views here.

def admins(request):
    return render(request, 'admins.html')


def getAddNews(request):
    return render(request, 'addNews.html')


def addNews(request):
    try:
        data = {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'type': request.POST.get('type'),
            'time': request.POST.get('time'),
            'context': request.POST.get('context'),
        }
        obj = models.News(**data)  # 保存对象
        obj.save()  # 保存对象
        return JsonResponse({'id': 1}, safe=False)  # 保存成功返回1
    except:
        return JsonResponse({'id': 0}, safe=False)


def getNewsList(request):
    return render(request, 'newsList.html')


def toDictNews(start, end, length):  # 把数据库类变为字典类
    objs = models.News.objects.all()[start:end]
    newObjs = [model_to_dict(_) for _ in objs]
    for i in range(end - start):
        newObjs[i].pop('context')
        newObjs[i]['id'] = length - start - i
    newObjs.reverse()
    return newObjs


def newsList(request):  # 处理新闻的请求
    # 由于数据随着时间时由后往前的，取数据需要注意
    page = int(request.GET.get('page'))
    limit = int(request.GET.get('limit'))
    objects_all = models.News.objects.all()
    length = objects_all.count()

    if page * limit > length:  # 如果超过总需求
        data = toDictNews(0, length - (page - 1) * limit, length)
    else:
        data = toDictNews(length - page * limit, length - (page - 1) * limit, length)
    return JsonResponse({"code": 0,
                         "msg": "返回成功",
                         "count": length,
                         'data': data})
