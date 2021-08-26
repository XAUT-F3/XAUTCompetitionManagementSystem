from django.conf.urls import url

# from uauth import views
from django.urls import path

from . import views, newsViews

urlpatterns = [
    path('', views.index),
    # url(r'^regist', views.regist),
    path('login/', views.login, name='login'),
    path('login.html/', views.login),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    # 用于加载新闻
    path('getFrontNews/', newsViews.getFrontNews, name='indexGetFrontNews'),
    path('indexNews/', newsViews.getIndexNews, name='indexNews'),   # 大赛动态首页
    path('indexNews/<int:id>/', newsViews.getOneNews, name='getOneNews'),  # 显示具体的一条新闻的页面


    path('getAllNewsLength/', newsViews.getAllNewsLength, name='getAllNewsLength'),  # 获取所有新闻总数目
    path('indexNewsDetails/', newsViews.getIndexNewsDetails, name='indexNewsDetails'),  # 获取所有新闻不同页面数据


]
