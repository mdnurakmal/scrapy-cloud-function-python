from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
    from os import path
def upload(myfile,destination):
    # Make an authenticated API request
    print("filename : " + myfile)
    print("destination : " + destination)

    root = path.dirname(path.abspath(__file__))
    children = os.listdir(root)
    files = [c for c in children if path.isfile(path.join(root, c))]
    return 'Files: {}'.format(files)

    # storage_client = storage.Client()
    # bucket = storage_client.bucket("afajof_calendar")

    # blob = bucket.blob(destination)
    # blob.upload_from_filename(myfile)
