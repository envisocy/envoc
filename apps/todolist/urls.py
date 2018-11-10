"""envoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodolistView, name='清单'),
    path('submit', views.TodolistSubmitView, name='编辑清单'),
    path('checked', views.TodolistCheckedView, name='完成状态切换'),
    path('delete', views.TodolistDeleteView, name='删除清单'),
    path('recycle', views.RecycleView, name='回收站'),
    path('recovery', views.TodolistRecoveryView, name='恢复清单'),
]
