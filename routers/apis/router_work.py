from http.client import HTTPException
from azure.storage.blob import BlobServiceClient ,BlobClient, __version__
from fastapi import APIRouter, HTTPException
from azure.identity import DefaultAzureCredential


router = APIRouter()

account_url = "https://hyperlogic.blob.core.windows.net/"
creds = DefaultAzureCredential()
service_client = BlobServiceClient(account_url=account_url,credential=creds)