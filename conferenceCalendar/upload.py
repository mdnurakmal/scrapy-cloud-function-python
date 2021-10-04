from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload():
    credentials_dict = {
        }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project='myproject')
    bucket = client.get_bucket('mybucket')
    blob = bucket.blob('myfile')
    blob.upload_from_filename('myfile')