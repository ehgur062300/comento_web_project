"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage),
    path('laptop/', views.laptop),
    path('company/', views.company),
    path('home/', views.home),
    path('search/', views.search),
    path('laptop_A/', views.laptop_A), path('laptop_B/', views.laptop_B), path('laptop_C/', views.laptop_C),
    path('tv/', views.tv),
    path('kitchen/', views.kitchen), path('beauty/', views.beauty), path('robot/', views.robot),
]
