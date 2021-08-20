from django.conf.urls import url

# from uauth import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # url(r'^regist', views.regist),
    path('login/', views.login),
    path('login.html/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup, name='signup'),
    # url(r'^upload', views.upload, name='upload'),
    # url(r'^index/', views.index),

]
