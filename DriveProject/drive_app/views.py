from django.http import JsonResponse, HttpResponse
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from django.views.decorators.csrf import csrf_exempt
from drive_app.utils import upload_on_drive

# Create your views here.
@csrf_exempt
def google_drive_upload(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST requests are allowed", "status": 405}, status=405)

    access_token = request.headers.get('Authorization')
    if not access_token:
        return JsonResponse({"error": "No access token provided"}, status=401)

    access_token = access_token.split(' ')[1]
    creds = Credentials(token=access_token)
    service = build("drive", "v3", credentials=creds)

    if not request.FILES:
        return JsonResponse({"error": "No files provided", "status": 400}, status=400)

    for key in request.FILES:
        files = request.FILES.getlist(key)
        if len(files) > 1:
            # Create a folder for multiple files
            folder_metadata = {
                'name': key,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            folder_id = folder.get('id')

            for file in files:
                file_metadata = {"name": file.name, "parents": [folder_id]}
                upload_on_drive(file, file_metadata, service)
        else:
            # Upload single file directly
            file = files[0]
            file_metadata = {"name": file.name}
            upload_on_drive(file, file_metadata, service)

    return JsonResponse({"message": "Successfully uploaded all files", "status": 200}, status=200)

