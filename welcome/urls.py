"""welcome URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views  # views.py:寫商業邏輯的地方，它會跟urls.py做呼應，並將所需傳達給前端
from .views import item_detail

urlpatterns = [
    path('home/', views.home, name='Home'),           # 首頁
    path('sign_up/', views.sign_up, name='Sign_up'),  # 註冊
    path('login/', views.sign_in, name='Sign_in'),    # 登入
    path('logout/', views.log_out, name='Logout'),    # 登出
    path('tenant/', views.tenant, name='Tenant'),    # 租房
    path('tenant_a/', views.tenant_a, name='Tenant_a'),    # 租房A_一般
    path('tenant_b/', views.tenant_b, name='Tenant_b'),    # 租房B_多選
    path('item/<str:item_id>/', views.item_detail, name='Item_detail'),  # 物件資料(動態生成頁面)
    path('group_tenant/', views.group_tenant, name='GroupTenant'),  # 合租
    path('join_group/', views.join_group, name='Join_group'),  # 加入合租
    path('leave_group/', views.leave_group, name='Leave_group'),  # 取消合租
    path('search_result/', views.search_house, name='search_house'),    # 租房
    path('analysis/', views.analysis, name='Analysis'),   # 分析
    path('rent_choose/', views.rent_choose, name='Rent_choose'),        # 出租
    path('rent_a/', views.rent_a, name='Rent_a'),        # 出租
    path('rent_b/', views.rent_b, name='Rent_b'),        # 出租
    path('rent_c/', views.rent_c, name='Rent_c'),        # 出租
    path('rent_d/', views.rent_d, name='Rent_d'),        # 出租
    path('about/', views.about, name='About'),      # 關於我們
]
