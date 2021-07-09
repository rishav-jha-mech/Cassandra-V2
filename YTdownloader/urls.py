from django.contrib import admin
from django.urls import path, include
from YTdownloader import views

urlpatterns=[
     path('',views.yt, name="home"),
     path('admin/', views.admin, name="admin"),
     path('accounts/admin/', views.accadmin, name="accadmin"),
]

