from fastapi import APIRouter

from routers.api_base import *

api_router = APIRouter()

api_router.include_router(router_test.router, prefix="/test", tags=["test"])