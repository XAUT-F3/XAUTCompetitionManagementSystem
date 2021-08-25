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
]
