from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload(myfile):
    # Make an authenticated API request
    client = storage.Client()
    bucket = storage.Bucket(client, "afajof_calendar", user_project="test-327905")

    blob.upload_from_filename(myfile)
    