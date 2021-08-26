from django.urls import path

from . import views

urlpatterns = [
    path('', views.admins, name='admins'),
    # 增加新闻
    path('getAddNews/', views.getAddNews, name='getAddNews'),
    path('addNews/', views.addNews, name='addNews'),
    # 新闻列表
    path('getNewsList/', views.getNewsList, name='getNewsList'),
    path('newsList/', views.newsList, name='newsList'),
    path('delNews/', views.delNews, name='delNews'),  # 删除新闻
    path('updateNews/<int:id>', views.updateNews, name='updateNews'),  # 获取更新新闻的页面
    path('updateNewsDetails', views.updateNewsDetails, name='updateNewsDetails')  # 更新页面的post请求
]
