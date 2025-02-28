from googleapiclient.http import MediaIoBaseUpload
import io

def upload_on_drive(file, file_metadata, service):
    media = MediaIoBaseUpload(io.BytesIO(file.read()), mimetype=file.content_type)
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    return uploaded_file