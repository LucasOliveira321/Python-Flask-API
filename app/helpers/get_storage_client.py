import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

def get_storage_client():
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    return storage.Client.from_service_account_json(credentials_path)
