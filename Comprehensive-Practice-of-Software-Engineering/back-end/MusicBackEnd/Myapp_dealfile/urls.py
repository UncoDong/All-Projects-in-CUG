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
from Myapp_dealfile import views

urlpatterns = [
    path('uploadindex/',views.show_uploadfile_index),       # 上传文件的首页
    path('uploadfile/',views.upload_file),       # 上传文件的接口
    path('downloadfile/<str:filename>',views.download_file), # 下载文件的接口
    path('dealfile/',views.deal_file),   # 处理文件的接口
]
#设置静态文件路径
#urlpatterns += staticfiles_urlpatterns()
