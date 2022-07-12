import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv()) # .env 파일의 환경변수 로드.


class Settings():
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER")
    DB_PORT = os.getenv("DB_PORT")

    DB_PATH = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    SECRET_KEY = os.getenv("SECRET_KEY") 
    ALGORITHM = os.getenv("ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    PROJECT_TITLE = "Workanalysis project"
    PROJECT_VERSION = "0.0.1"
    
settings = Settings()