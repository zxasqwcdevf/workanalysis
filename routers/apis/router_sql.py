from fastapi import APIRouter, HTTPException, FastAPI, Depends
from sqlalchemy.orm.session import Session
from database.query.base import work
from fastapi.responses import JSONResponse

from database.database import get_db

router = APIRouter()

@router.get('/work/', description='쿼리 테스트 용입니다')
async def test(db:Session =Depends(get_db)):
    data = work(db = db)
    return data

@router.get("/read/", description='코멘트 확인용 API입니다.')
async def get_comment_by_id(seq: str, db: Session = Depends(get_db)):
    data = work(db, seq)
    json_data = work(data)
    return JSONResponse(content=json_data)