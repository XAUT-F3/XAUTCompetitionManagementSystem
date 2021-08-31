from django.urls import path

from . import views, competitionViews, teamViews

urlpatterns = [
    path('', views.admins, name='admins'),
    # 增加新闻
    path('getAddNews/', views.getAddNews, name='getAddNews'),
    path('addNews/', views.addNews, name='addNews'),
    # 新闻列表
    path('getNewsList/', views.getNewsList, name='getNewsList'),
    path('newsList/', views.newsList, name='newsList'),
    path('delNews/', views.delNews, name='delNews'),  # 删除新闻
    path('updateNews/<int:id>/', views.updateNews, name='updateNews'),  # 获取更新新闻的页面
    path('updateNewsDetails/', views.updateNewsDetails, name='updateNewsDetails'),  # 更新页面的post请求

    # 竞赛管理模块
    path('teamList/', teamViews.teamList, name='teamList'),
    path('getTeamList/', teamViews.getTeamList, name='getTeamList'),
    path('getTeamListCSV/', teamViews.getTeamListCSV, name='getTeamListCSV'),
    path('updateTeamDetails/', teamViews.updateTeamDetails, name='updateTeamDetails'),


    path('adminsDelTeam/', teamViews.adminsDelTeam, name='adminsDelTeam'),
    path('adminsDetailsTeam/<int:team_id>/', teamViews.adminsDetailsTeam, name='adminsDetailsTeam'),
    path('adminsAddMember/', teamViews.adminsAddMember, name='adminsAddMember'),

    # competition

    path('studentdata/', competitionViews.studentdata),
    path('studentdata/csv', competitionViews.studentdatacsv),
    path('teacherdata/', competitionViews.teacherdata),
    path('teacherdata/csv', competitionViews.teacherdatacsv),
    path('teamdata', competitionViews.teamdata),
    path('teamdata/csv', competitionViews.teamdatacsv),
]
