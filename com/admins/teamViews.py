import codecs
import csv
import time
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from apply.models import Race_name, Race_Message, Team, Member, Honor
from apply.views import searchMember
from uauth.models import teachers, students


def teamList(request):
    return render(request, 'teamList.html', {'raceName': Race_name.objects.all()})


def getData(request):
    """
        在此处查看所有队伍信息处理复杂因此做出以下注释
        首先通过race_id查看所有所有有关的赛事id
        接下来通过赛事id查看所有比赛队伍，此处可以获取队长姓名和电话
        接下来可以查看member成员
        """
    race_id = int(request.GET.get('race_id'))
    messages = Race_Message.objects.filter(m_race=race_id)
    teams = []
    for message in messages:
        teams += Team.objects.filter(T_message=message.id)  # 获取到了所有队伍
    data = []
    for team in teams:
        all_student = Member.objects.filter(team_id=team.id, type=0)  # 所有学生
        all_teacher = Member.objects.filter(team_id=team.id, type=1)  # 所有老师
        teachersName, studentsName = '', ''
        for stu in all_student:
            studentsName += students.objects.get(id=stu.member_id).s_name + ','
        for tea in all_teacher:
            teachersName += teachers.objects.get(id=tea.member_id).t_name + ','
        race_name = Race_Message.objects.get(id=team.T_message).m_name
        data.append({'id': team.id, 'raceName': race_name, 'teamName': team.T_name, 'captain': team.T_leader,
                     'phone': team.T_phone,
                     'member': studentsName, 'instructor': teachersName, 'state': team.T_state, 'honor': team.T_honor})
    return data


def getTeamList(request):  # 查看所有参赛队伍
    data = getData(request)
    length = len(data)
    limit = int(request.GET.get('limit'))
    page = int(request.GET.get('page'))
    if limit * page > length:
        data = data[(page - 1) * limit:length]
    else:
        data = data[(page - 1) * limit:page * limit]
    return JsonResponse({"code": 0,
                         "msg": "返回成功",
                         "count": length,
                         'data': data})


def getTeamListCSV(request):
    data = getData(request)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment;filename = "{int(time.time())}.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['所属赛道', '队伍名称', '队长', '队长电话', '队伍成员', '指导老师', '队伍状态', '荣誉'])
    for b in data:
        writer.writerow(
            [b['raceName'], b['teamName'], b['captain'], b['phone'], b['member'], b['instructor'], b['state'],
             b['honor']])
    return response


def adminsDelTeam(request):
    try:
        team_id = request.GET.get('team_id')
        Team.objects.get(id=team_id).delete()
        Member.objects.filter(team_id=team_id).delete()
        return JsonResponse({'msgs': '删除成功！'})
    except:
        return JsonResponse({'msgs': '服务器繁忙，请稍后尝试！'})


def adminsDetailsTeam(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
        race = Race_Message.objects.get(id=team.T_message)  # 查到的小赛题
        bigRace = Race_name.objects.get(id=race.m_race)
        all_honor = Honor.objects.all()
        all_student = Member.objects.filter(team_id=team_id, type=0)  # 所有学生
        all_teacher = Member.objects.filter(team_id=team_id, type=1)  # 所有老师
        teacherList = [teachers.objects.get(id=_.member_id) for _ in all_teacher]
        studentList = [students.objects.get(id=_.member_id) for _ in all_student]
        data = {'teamID': team_id, 'raceName': bigRace.r_name, 'messageName': race.m_name, 'teamName': team.T_name,
                'teamIntro': team.T_intro, 'captain': team.T_leader, 'captainPhone': team.T_phone,
                'state': team.T_state, 'honor': team.T_honor, 'slogan': team.T_slogan, 'remark': team.T_remark,
                'studentList': studentList, 'teacherList': teacherList, 'allHonor': all_honor}
        return render(request, 'teamDetail.html', data)
    except:
        return render(request, '404.html')


def updateTeamDetails(request):
    try:
        team_id = request.POST.get('team_id')
        team = Team.objects.filter(id=team_id)
        captain_phone = request.POST.get('captainPhone')
        captain = request.POST.get('captain')
        if len(students.objects.filter(s_phone=captain_phone, s_name=captain)) == 0:
            return HttpResponse('<script>alert("未查询到该用户！")</script>')
        team.update(
            T_leader=captain,
            T_phone=captain_phone,
            T_name=request.POST.get('raceName'),
            T_intro=request.POST.get('teamIntro'),
            T_state=request.POST.get('state'),
            T_honor=request.POST.get('honor'),
            T_slogan=request.POST.get('slogan'),
            T_remark=request.POST.get('remark')
        )
        return adminsDetailsTeam(request, team_id)
    except:
        return render(request, '404.html')


def adminsAddMember(request):
    try:
        obj, phone, team_id, type = searchMember(request)
        if len(obj) == 0:
            return JsonResponse({'code': 0, 'msgs': '未查询到该用户'})  # 报名失败返回0
        elif len(Member.objects.filter(member_id=obj[0].id, team_id=team_id)) != 0:
            return JsonResponse({'code': 0, 'msgs': '该用户已存在于队伍中'})  # 报名失败返回0
        Member.objects.create(team_id=team_id, invite_state=0, member_id=obj[0].id, type=type)  # 默认状态为0，等待对方确认
        return JsonResponse({'code': 1, 'msgs': '成功发出邀请，等待对方确认~', 'type': type})
    except:
        return JsonResponse({'code': 0, 'msgs': '服务繁忙，请稍后重试！'})
