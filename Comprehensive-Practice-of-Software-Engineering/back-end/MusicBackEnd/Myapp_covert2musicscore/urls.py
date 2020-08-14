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
from Myapp_covert2musicscore import views
urlpatterns = [
    path('uploadstr/',views.show_uploadstr_index),       # 上传字符串的页面
    path('changestr2pic/',views.convert_musicstr_2_pic), # 将字符串转换成pic
    path('testimages/',views.test_show_pic),   # 测试图片显示
    path('showfromuser/',views.show_from_user),   # 测试图片显示
]
#设置静态文件路径
#urlpatterns += staticfiles_urlpatterns()
