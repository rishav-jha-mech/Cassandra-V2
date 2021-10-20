from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler500


urlpatterns = [
    path('RohiniBose/', admin.site.urls),
    path('', include("YTdownloader.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'YTdownloader.views.handler404'
handler500 = 'YTdownloader.views.handler500'
