from django.urls import path, include
from drive_app.views import google_drive_upload

urlpatterns = [
    path('upload/', google_drive_upload),
]