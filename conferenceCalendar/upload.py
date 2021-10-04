from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload(myfile,destination):
    # Make an authenticated API request

    storage_client = storage.Client()
    bucket = storage_client.bucket("afajof_calendar")

    blob = bucket.blob(destination)
    blob.upload_from_filename(myfile)
