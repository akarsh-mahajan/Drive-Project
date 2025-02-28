from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow
from django.http import JsonResponse
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from DriveProject.settings import CLIENT_SECRETS_FILE
import os


flow = Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
    redirect_uri="http://127.0.0.1:8000/auth/callback/"
)

def google_login(request):
    auth_url, _ = flow.authorization_url(prompt="consent")
    return redirect(auth_url)

def google_callback(request):
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    return JsonResponse({"access_token": credentials.token})