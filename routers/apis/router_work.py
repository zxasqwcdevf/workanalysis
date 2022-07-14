from http.client import HTTPException
from azure.storage.blob import BlobServiceClient ,BlobClient, __version__
from fastapi import APIRouter, HTTPException
from azure.identity import DefaultAzureCredential


router = APIRouter()

account_url = "https://hyperlogic.blob.core.windows.net/"
creds = DefaultAzureCredential()
service_client = BlobServiceClient(account_url=account_url,credential=creds)


@router.get("/workpeople/", description='구인동향 분석')
async def read_workpeople():
    container_name="workanalysis"
    blob_name = f'한국_산업_인력_공단/구인_동향_분석/총괄_고용형태_지역_신규_구인건수.json'
    blob_url = f"{account_url}/{container_name}/{blob_name}"

    blob_client = BlobClient.from_blob_url(blob_url=blob_url,credential=creds)
    blob_download = blob_client.download_blob()

    try:
        blob_download.readall()
        return f"https://hyperlogic.blob.core.windows.net/work_analysis/한국_산업_인력_공단/구인_동향_분석/총괄_고용형태_지역_신규_구인건수.json"
    except HTTPException:
        HTTPException(status_code=404,detail="File not found")


@router.get("/region/", description='구인동향 분석')
async def read_workpeople():
    container_name="workanalysis"
    blob_name = f'한국_산업_인력_공단/구인_동향_분석/구인구직_연월_지역.csv'
    blob_url = f"{account_url}/{container_name}/{blob_name}"

    blob_client = BlobClient.from_blob_url(blob_url=blob_url,credential=creds)
    blob_download = blob_client.download_blob()

    try:
        blob_download.readall()
        return f"https://hyperlogic.blob.core.windows.net/work_analysis/한국_산업_인력_공단/구인_동향_분석/구인구직_연월_지역.csv"
    except HTTPException:
        HTTPException(status_code=404,detail="File not found")

@router.get("/test/", description='구인동향 분석')
async def read_workpeople():
    container_name="workanalysis"
    blob_name = f'한국_산업_인력_공단/구인_동향_분석/구인구직_연월_지역.csv'
    blob_url = f"{account_url}/{container_name}/{blob_name}"

    blob_client = BlobClient.from_blob_url(blob_url=blob_url,credential=creds)
    blob_download = blob_client.download_blob()

    try:
        blob_download.readall()
        return f"https://hyperlogic.blob.core.windows.net/work_analysis/한국_산업_인력_공단/구인_동향_분석/구인구직_연월_지역.csv"
    except HTTPException:
        HTTPException(status_code=404,detail="File not found")