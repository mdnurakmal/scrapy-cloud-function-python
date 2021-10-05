from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload(myfile,destination):
    # Make an authenticated API request
    print("filename : " + myfile)
    print("destination : " + destination)


    storage_client = storage.Client()
    bucket = storage_client.bucket("afajof_calendar")

    blob = bucket.blob(destination)
    blob.upload_from_filename(myfile)
