from http.client import HTTPException
from azure.storage.blob import BlobServiceClient ,BlobClient, __version__
from fastapi import APIRouter, HTTPException
from azure.identity import DefaultAzureCredential


router = APIRouter()

account_url = "https://hyperlogic.blob.core.windows.net/"
creds = DefaultAzureCredential()
service_client = BlobServiceClient(account_url=account_url,credential=creds)

@router.get("/raw_data")
async def download():
    container_name="workanalysis"
    blob_name = f'한국_산업_인력_공단/raw_data/총괄_고용형태_지역.csv'
    blob_url = f"{account_url}/{container_name}/{blob_name}"
    
    blob = BlobClient.from_blob_url(blob_url=blob_url,credential=creds)
    
    try:
        with open("./총괄_고용형태_지역.csv", "wb") as my_blob:
            blob_data = blob.download_blob()
            blob_data.readinto(my_blob)
            return f"https://hyperlogic.blob.core.windows.net//workanalysis/한국_산업_인력_공단/raw_data/총괄_고용형태_지역.csv"
    except HTTPException:
        HTTPException(status_code=404,detail="File not found")

        
