from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os

def upload():
    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
    # bucket = client.get_bucket('afajof_calendar')
    # blob = bucket.blob('myfile')
    # blob.upload_from_filename('myfile')