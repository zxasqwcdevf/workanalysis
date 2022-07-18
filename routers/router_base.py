from fastapi import APIRouter

from routers.api_base import *

api_router = APIRouter()

api_router.include_router(router_rawdata.router, prefix="/raw_data", tags=["data"])

api_router.include_router(router_jobSearch.router, prefix="/jobSearch", tags=["jobSearch"])