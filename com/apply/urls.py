from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index,),
    # url(r'^signup', views.signup, name='signup'),
    path('', views.apply, name='applyHome'),
    # url(r'^apply/(\d+)/$', views.race_message)
    path('race_message/', views.race_message, name='applyMessages'),  # 获取赛事信息
    path('self_message/', views.self_message, name='selfMessages'),  # 获取个人信息
    path('confirm_self/', views.confirm_self),
    path('team/', views.team, name='applyTeam'),  # 提交队伍信息
    path('addMatchStudent/', views.addMatchStudent, name='addMatchStudent'),  # 提交队伍信息
    path('deleteMessage/<int:id>/', views.deleteMessage, name='deleteMessage')  # 删除个人参赛信息
]
