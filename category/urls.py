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
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('product/create/<int:product_id>/', views.product_create, name='product_create'),
    # path('product/update/<int:product_id>/', views.product_update,name='product_update'),
    # path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),

    path(r'^post/(?P<id>[0-9]+)/$', views.postview, name = 'post'),
    path('tv/', views.tv), path('laptop/', views.laptop), path('kitchen/', views.kitchen),
    path('beauty/', views.beauty), path('robot/', views.robot),
]

