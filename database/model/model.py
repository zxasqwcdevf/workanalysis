from sqlalchemy import Column,Boolean, Integer, Float, String, DateTime
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Date, Time
from ..database import Base
from pydantic.main import BaseModel

# 데이터베이스 모델 작성 및 테이블 생성 코드

# DB 컬렴명과 변수명을 일치시켜야함. - 테이블 생성도 가능.

# 주의사항 - 모든 테이블에는 Primary 키가 존재해야함. - 키가 없는 테이블에도 Primary key인것처럼 우회해서 사용해야함.
#
# There is only one way that I know of to circumvent the primary key constraint in SQL Alchemy
# - it's to map specific column or columns to your table as a primary keys,
# even if they aren't primary key themselves.