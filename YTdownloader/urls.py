from django.urls import path, include
from YTdownloader import views

urlpatterns=[
     path('',views.yt, name="home"),
]

