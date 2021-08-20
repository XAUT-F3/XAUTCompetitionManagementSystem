from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from uauth.models import Users
from django.shortcuts import render
from django.http import HttpResponse


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 统一验证登录
        # return none 或者 不写return才会继续往下执行, 不需要执行
        if request.path == '/login/' or request.path == '/signup/' or request.path == '/':
            return None
            # return HttpResponseRedirect('/index/')
            # return render(request, 'index.html')

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
            # return HttpResponse("失败！")
            # return None
            # return HttpResponseRedirect('/index/')
        users = Users.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/login/')
            # return None
            # return HttpResponseRedirect('/index/')
        # 将user赋值在request请求的user上，以后可以直接判断user有没有存在
        # 备注，django自带的有user值
        request.user = users[0]
        # request.users
