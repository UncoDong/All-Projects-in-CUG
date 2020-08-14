"""MusicBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from Myapp_runweb import views

urlpatterns = [
    path('home/',views.home),       # 展示主页
    path('str2musicscore/',views.str_to_musicscore), # 显示钢琴页面
    path('wavescope/',views.wave_scope), # 波形图
    path('pianoOnLine/',views.piano_online), # 在线钢琴
    path('metronome/',views.metronome), # 节拍器
    path('file2musicscore/',views.file_to_musicscore), # 节拍器
    path('login/',views.login),       # 登录
     path('register/',views.register),       # 登录
     path('delscore/',views.del_score),       # 登录

]
#设置静态文件路径
#urlpatterns += staticfiles_urlpatterns()
