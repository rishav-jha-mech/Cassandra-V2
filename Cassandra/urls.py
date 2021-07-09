from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404,handler500


urlpatterns = [
    path('RohiniBose/', admin.site.urls),
    path('', include("YTdownloader.urls"))
]

handler404 = 'YTdownloader.views.handler404'
handler500 = 'YTdownloader.views.handler500'
