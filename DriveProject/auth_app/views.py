from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow
from django.http import JsonResponse, HttpResponse
from DriveProject.settings import CLIENT_SECRETS_FILE
from django.shortcuts import render

def api_documentation(request):
    return render(request, 'index.html')

flow = Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/drive.file"],
    redirect_uri="http://127.0.0.1:8000/auth/callback/"
)

def google_login(request):
    auth_url, _ = flow.authorization_url(prompt="consent")
    return redirect(auth_url)

def google_callback(request):
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    return JsonResponse({
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "status": 200
    }, status=200)

