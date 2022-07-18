from sqlalchemy.orm import Session

def employ(db:Session ,year:str, month:str):
    sql = f"""
   SELECT
	"5_구인구직취업현황_고용형태"."연도", 
	"5_구인구직취업현황_고용형태"."월", 
	"5_구인구직취업현황_고용형태"."고용형태", 
	"5_구인구직취업현황_고용형태"."구인인원", 
	"5_구인구직취업현황_고용형태"."구직건수", 
	"5_구인구직취업현황_고용형태"."취업건수"
    FROM
	"인력수급현황"."5_구인구직취업현황_고용형태"
    WHERE 
    "5_구인구직취업현황_고용형태"."연도"::text = '{year}'::text AND "5_구인구직취업현황_고용형태"."월" = '{month}'::text
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def industry(db:Session):
    sql = f"""
    SELECT
    FROM
    GROUP BY
    ORDER BY
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def gendered(db:Session,year:str, month:str):
    sql = f"""
    SELECT
	"1_구직취업현황_성별"."연도", 
	"1_구직취업현황_성별"."월", 
	"1_구직취업현황_성별"."성별", 
	"1_구직취업현황_성별"."구직건수", 
	"1_구직취업현황_성별"."취업건수"
    FROM
	"인력수급현황"."1_구직취업현황_성별"
    WHERE
	"1_구직취업현황_성별"."연도" = '{year}' AND
	"1_구직취업현황_성별"."월" = '{month}'
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def age(db:Session):
    sql = f"""
    SELECT
    FROM
    GROUP BY
    ORDER BY
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result 

def job(db:Session):
    sql = f"""
    SELECT
    FROM
    GROUP BY
    ORDER BY
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result


def education(db:Session):
    sql = f"""
    SELECT
    FROM
    GROUP BY
    ORDER BY
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result