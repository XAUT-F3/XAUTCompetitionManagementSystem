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
    path('indexNews/', newsViews.getIndexNews, name='indexNews'),
    path('getAllNewsLength/', newsViews.getAllNewsLength, name='getAllNewsLength'),

    path('showNews/', newsViews.getOneNews, name='getOneNews'),  # 显示具体的一条新闻
    path('showNewsContext/', newsViews.getNewsContext, name='newsContexts')  # 显示具体的一条新闻
    # url(r'^upload', views.upload, name='upload'),
    # url(r'^index/', views.index),

]
