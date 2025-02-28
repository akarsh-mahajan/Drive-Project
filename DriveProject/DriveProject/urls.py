from django.contrib import admin
from django.urls import path, include
from auth_app.views import google_login, google_callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', google_login),
    path('auth/callback/', google_callback),
    # path('drive/', include('drive_app.urls')),
    # path('chat/', include('chat_app.urls')),
]
