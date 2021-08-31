from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('personalCenter/', views.getMessage, name='personalCenter'),
    path('changeSelf/', views.changeSelf, name='changeSelf'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('self/', views.self, name='self'),
]
