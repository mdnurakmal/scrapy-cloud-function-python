from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload():
    # Make an authenticated API request
    client = storage.Client()
    bucket = storage.Bucket(client, "afajof_calendar", user_project="test-327905")
    all_blobs = list(client.list_blobs(bucket))


    print(all_blobs)

    # bucket = client.get_bucket('afajof_calendar')
    # blob = bucket.blob('myfile')
    # blob.upload_from_filename('myfile')