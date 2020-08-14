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
from django.urls import path,include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('Myapp_dealfile/', include('Myapp_dealfile.urls')),
    path('Myapp_covert2musicscore/', include('Myapp_covert2musicscore.urls')),
    path('Myapp_runweb/', include('Myapp_runweb.urls')),
    path('Myapp_login/', include('Myapp_login.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico',RedirectView.as_view(url=r'static/favicon.ico')),
]

from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
