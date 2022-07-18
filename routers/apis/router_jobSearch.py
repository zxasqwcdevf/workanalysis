from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.query.base import *

from database.database import get_db

router = APIRouter()

@router.get('/gender/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def gender(year='2018', month='01', db:Session =Depends(get_db)):
    data = gendered(db,year,month)
    result =[]
    year,month,gender,tmp1,tmp2 = [],[],[],[],[]
    length = len(data)
    col_name = ["연도","월","성별","구직건수", "취업건수"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        gender.append(data[i]["성별"])
        tmp1.append(data[i]["구직건수"])
        tmp2.append(data[i]["취업건수"])
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(gender)
    result.append(tmp1)
    result.append(tmp2)
    return result

@router.get('/age/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def age(year='2018', month='01', db:Session =Depends(get_db)):
    data = aged(db,year,month)
    result =[]
    year,month,age,tmp1,tmp2 = [],[],[],[],[]
    length = len(data)
    col_name = ["연도","월","연령","구직건수", "취업건수"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        age.append(data[i]["연령"])
        tmp1.append(data[i]["구직건수"])
        tmp2.append(data[i]["취업건수"])
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(age)
    result.append(tmp1)
    result.append(tmp2)
    return result

@router.get('/education/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def education(year='2018', month='01', db:Session =Depends(get_db)):
    data = educationed(db,year,month)
    result =[]
    year,month,edu,tmp1,tmp2,tmp3 = [],[],[],[],[],[]
    length = len(data)
    col_name = ["연도","월","학력","구인인원","구직건수", "취업건수"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        edu.append(data[i]["학력"])
        tmp1.append(data[i]["구인인원"])
        tmp2.append(data[i]["구직건수"])
        tmp3.append(data[i]["취업건수"])
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(edu)
    result.append(tmp1)
    result.append(tmp2)
    result.append(tmp3)
    return result


@router.get('/employ/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def employ(year='2018', month='01' ,db:Session =Depends(get_db)):
    data = employed(db,year,month)
    result =[]
    year,month,emp,tmp1,tmp2,tmp3 = [],[],[],[],[],[]
    length = len(data)
    col_name = ["연도","월","고용형태","구인인원","구직건수", "취업건수"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        emp.append(data[i]["고용형태"])
        tmp1.append(data[i]["구인인원"])
        tmp2.append(data[i]["구직건수"])
        tmp3.append(data[i]["취업건수"])
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(emp)
    result.append(tmp1)
    result.append(tmp2)
    result.append(tmp3)
    return result

@router.get('/industry/', description='성별 구직건수와 취업건수 합계를 보여줍니다.')
async def industry(year='2018', month='01' ,db:Session =Depends(get_db)):
    data = industried(db,year,month)
    result =[]
    year,month,ind,tmp1,tmp2 = [],[],[],[],[]
    length = len(data)
    col_name = ["연도","월","산업_대분류","구인인원(월)", "취업건수(월)"]
    for i in range(length):
        year.append(data[i]["연도"])
        month.append(data[i]["월"])
        ind.append(data[i]["산업_대분류"])
        tmp1.append(data[i]["구인인원(월)"])
        tmp2.append(data[i]["취업건수(월)"])
        tmp2 * -1
    result.append(col_name)
    result.append(year)
    result.append(month)
    result.append(ind)
    result.append(tmp1)
    result.append(tmp2)
    return result