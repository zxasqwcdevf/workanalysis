from fastapi import (FastAPI,
 Request)
from fastapi.middleware.cors import CORSMiddleware
from core.config import Settings
from database.database import engine, Base
from database.schemas import *
from database.query.base import *

from routers.router_base import api_router


origins = ["*"]


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(
        title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION
    )
    include_router(app)
    create_tables()
    return app

app = start_app()

@app.middleware("http")
async def add_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response

@app.get("/")
async def index():
    return 'If you can see this msg, server is running well.'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)