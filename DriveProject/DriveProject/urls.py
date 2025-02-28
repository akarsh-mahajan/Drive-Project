from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('auth_app.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('drive/', include('drive_app.urls')),
]
