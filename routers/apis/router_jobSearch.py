from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.query.base import *

from database.database import get_db

router = APIRouter()

@router.get('/gender/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def gender(year='2018',month='01' ,db:Session =Depends(get_db)):
    data = gendered(db,year,month)
    result =[]
    year,month,tmp1,tmp2 = [],[],[],[]
    length = len(data)
    col_name = ["연도","월","구직건수", "취업건수"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        tmp1.append(data[i]["구직건수"])
        tmp2.append(data[i]["취업건수"])
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(tmp1)
    result.append(tmp2)
    return result

