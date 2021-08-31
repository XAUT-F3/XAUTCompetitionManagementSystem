from django.shortcuts import render

# Create your views here.
from apply.models import Race_name, Race_Message, Team, Member
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from uauth.models import Users, students, teachers
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password, check_password


def getMessage(request):
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    phone = users.u_phone  # 从页面获取登录用户的手机号
    sid = students.objects.get(s_phone=phone).id
    teamMessages = Team.objects.filter(T_phone=phone)  # 作为队长的所有队伍
    lengthOne = len(teamMessages)
    raceMessagesList = []
    raceNamesList = []
    membersList = []
    for i in range(0, lengthOne):
        race_id = teamMessages[i].T_message
        raceMessage = Race_Message.objects.get(id=race_id)  # 获取赛题名称
        raceMessagesList.append(raceMessage)
        raceName = Race_name.objects.get(id=raceMessage.m_race)  # 获取赛事名称
        raceNamesList.append(raceName)
        members_id = Member.objects.filter(team_id=teamMessages[i].id)  # 获取成员信息
        memberList = []
        for member in members_id:
            s_id = students.objects.get(id=member.member_id)
            memberList.append(s_id)
        membersList.append(memberList)
    all1 = zip(teamMessages, raceMessagesList, raceNamesList, membersList)

    teamMessages = Member.objects.filter(member_id=sid)  # 获取作为队员的所有队伍id
    lengthTwo = len(teamMessages)
    teamMessages2List = []
    raceMessagesList2 = []
    raceNamesList2 = []
    membersList2 = []
    for i in range(0, lengthTwo):
        teamMessages_id = teamMessages[i].team_id
        teamMessage2 = Team.objects.get(id=teamMessages_id)  # 获取队伍信息
        teamMessages2List.append(teamMessage2)
        raceMessage2 = Race_Message.objects.get(id=teamMessage2.T_message)  # 获取赛题信息
        raceMessagesList2.append(raceMessage2)
        raceName2 = Race_name.objects.get(id=raceMessage2.m_race)  # 获取赛事信息
        raceNamesList2.append(raceName2)
        members_id2 = Member.objects.filter(team_id=teamMessages_id)
        memberList2 = []
        for member2 in members_id2:
            s_id2 = students.objects.get(id=member2.member_id)
            memberList2.append(s_id2)
        membersList2.append(memberList2)
    all2 = zip(teamMessages2List, raceMessagesList2, raceNamesList2, membersList2)

    return render(request, 'personalCenter.html', {'all1': all1, "all2": all2, 'users': users})


def changeLeader(request):
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    sid = request.GET.get('sid')  # 返回成员id
    tid = request.GET.get('tid')  # 返回队伍id
    m_stu = students.objects.get(id=id)
    Team.objects.filter(id=tid).update(T_leader=users.u_name, T_phone=users.u_phone)
    Member.objects.filter(id=sid).update(member_id=m_stu)


def deleteTeam(request):
    tid = request.GET.get('tid')  # 返回队伍id
    Member.objects.filter(team_id=tid).delete()
    Team.objects.get(id=tid).delete()


def self(request):
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    phone = users.u_phone  # 从页面获取登录用户的手机号
    stu = students.objects.get(s_phone=phone)
    return render(request, 'change_self.html', {'stu': stu, 'users': users})


def changeSelf(request):  # 修改个人信息
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    phone = users.u_phone
    stu = students.objects.get(s_phone=phone)
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
    phone2 = request.POST.get('s_phone')
    students.objects.filter(s_phone=phone).update(s_name=s_name)
    students.objects.filter(s_phone=phone).update(s_picture=picture)
    students.objects.filter(s_phone=phone).update(s_sex=sex)
    students.objects.filter(s_phone=phone).update(s_certification_type=certification_type)
    students.objects.filter(s_phone=phone).update(s_id_number=id_number)
    students.objects.filter(s_phone=phone).update(s_politics_status=politics_status)
    students.objects.filter(s_phone=phone).update(s_college=college)
    students.objects.filter(s_phone=phone).update(s_grade=grade)
    students.objects.filter(s_phone=phone).update(s_class=s_class)
    students.objects.filter(s_phone=phone).update(s_number=number)
    students.objects.filter(s_phone=phone).update(s_mail=mail)
    # students.objects.filter(s_phone=phone).update(s_birthday=birthday)
    students.objects.filter(s_phone=phone).update(s_phone=phone2)
    filePath = os.path.join(settings.MEDIA_ROOT, picture.name)
    with open(filePath, 'wb') as fp:
        for info in picture.chunks():
            fp.write(info)
    stu = students.objects.get(s_phone=phone2)
    return render(request, 'change_self.html', {'stu': stu, 'users': users})


def changePassword(request):
    ticket = request.COOKIES.get('ticket')
    users = Users.objects.get(u_ticket=ticket)
    oldPassword = request.POST.get('oldPassword')
    if check_password(oldPassword, users.u_password):
        newPassword1 = request.POST.get('newPassword1')
        newPassword2 = request.POST.get('newPassword2')
        if newPassword1 == newPassword2:
            password = make_password(newPassword2)
            Users.objects.filter(u_phone=users.u_phone).update(u_password=password)
            # return render(request,'changePassword.html'，'修改成功')
            return render(request, 'changePassword.html', {"is_change": 1, "users": users})
        else:
            return render(request, 'changePassword.html', {"is_login": 0, "users": users})
    else:
        # return render(request,'changePassword.html','修改失败')
        return render(request, 'changePassword.html', {"is_login": 2, "users": users})
