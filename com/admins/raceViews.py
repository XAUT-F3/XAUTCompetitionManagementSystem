import time
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from apply.models import Race_name, Race_Message, Team, Member, Honor


def raceList(request):
    return render(request, 'raceList.html')


def getRaceList(request):
    race = Race_name.objects.all()
    data = [{'id': _.id, 'raceName': _.r_name, 'startTime': str(_.start_date), 'endTime': str(_.end_date)} for _ in
            race]
    return JsonResponse({
        "code": 0,
        "msg": "返回成功",
        "count": race.count(),
        'data': data
    })


def addRace(request):
    return render(request, 'addRaces.html')


def addRaceDetails(request):
    try:
        data = {
            'r_name': request.POST.get('name'),
            'start_date': request.POST.get('startTime'),
            'end_date': request.POST.get('endTime')
        }
        Race_name(**data).save()
        return HttpResponse('<script>alert("添加成功！")</script>')
    except:
        return HttpResponse('<script>alert("服务器繁忙！")</script>')


def addMessageDetail(request):
    id = request.GET.get('id')
    return render(request, 'raceDetail.html', {'id': id, 'name': Race_name.objects.get(id=id).r_name})


def getMessageData(request):
    return {
        'm_race': request.POST.get('id'),
        'm_name': request.POST.get('name'),
        'm_content': request.POST.get('content'),
        'm_signup_request': request.POST.get('signupRequest'),
        'm_work_request': request.POST.get('workRequest')
    }


def addMessageAndChangeDetails(request):
    try:
        data = getMessageData(request)
        Race_Message(**data).save()
        return HttpResponse('<script>alert("添加成功！")</script>')
    except:
        return HttpResponse('<script>alert("服务器繁忙！")</script>')


def raceUpdateDetails(request):
    id = request.GET.get('id')
    objs = Race_Message.objects.filter(m_race=id)
    return render(request, 'raceUpdateDetail.html', {'objs': objs, 'name': Race_name.objects.get(id=id).r_name})


def raceUpdateDetailsFunction(request):
    try:
        data = getMessageData(request)
        obj = Race_Message.objects.filter(id=data['m_race'])
        obj.update(m_name=data['m_name'], m_content=data['m_content'], m_signup_request=data['m_signup_request'],
                   m_work_request=data['m_work_request'])
        return HttpResponse('<script>alert("修改成功！")</script>')
    except:
        return render(request, '404.html')


def deleteRaceMessage(request):
    try:
        # Race_Message.objects.get(id=int(request.GET.get('id'))).delete()
        return JsonResponse({'code': 1})
    except:
        return JsonResponse({'code': 0})
