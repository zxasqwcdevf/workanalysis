from http.client import HTTPException
from azure.storage.blob import BlobServiceClient ,BlobClient, __version__
from fastapi import APIRouter, HTTPException
from azure.identity import DefaultAzureCredential


router = APIRouter()

account_url = "https://hyperlogic.blob.core.windows.net/"
creds = DefaultAzureCredential()
service_client = BlobServiceClient(account_url=account_url,credential=creds)

@router.get("")
async def read_work():
    container_name="workanalysis"
    blob_name = f'지역별/총괄_고용형태_지역.csv'
    blob_url = f"{account_url}/{container_name}/{blob_name}"

    blob_client = BlobClient.from_blob_url(blob_url=blob_url,credential=creds)
    blob_download = blob_client.download_blob()

    try:
        blob_download.readall()
        return 1
    except HTTPException:
        HTTPException(status_code=404,detail="File not found")
