from django.urls import path, include
from auth_app.views import api_documentation, google_login, google_callback

urlpatterns = [
    path('', api_documentation),
    path('login/', google_login),
    path('callback/', google_callback),
]
