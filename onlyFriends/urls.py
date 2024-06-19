from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homie_activities.urls')),
    path('api/v1/', include('utils.urls')),
]
