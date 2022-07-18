from sqlalchemy.orm import Session

def employed(db:Session ,year:str, month:str):
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
    "5_구인구직취업현황_고용형태"."연도" = '{year}' AND 
    "5_구인구직취업현황_고용형태"."월" = '{month}'
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def industried(db:Session, year:str, month:str):
    sql = f"""
    SELECT
	    "6_구인취업현황_산업분류"."연도", 
	    "6_구인취업현황_산업분류"."월", 
	    "6_구인취업현황_산업분류"."산업_대분류", 
	    "6_구인취업현황_산업분류"."구인인원(월)", 
	    "6_구인취업현황_산업분류"."취업건수(월)" *-1 AS "취업건수(월)"
    FROM
	    "인력수급현황"."6_구인취업현황_산업분류"
    WHERE
	    "6_구인취업현황_산업분류"."연도" = '{year}' AND
	    "6_구인취업현황_산업분류"."월" = '{month}'
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
	    "1_구직취업현황_성별"."취업건수" *-1 AS "취업건수"
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

def aged(db:Session,year:str,month:str):
    sql = f"""
    SELECT
	    "2_구직취업현황_연령"."연도", 
	    "2_구직취업현황_연령"."월", 
	    "2_구직취업현황_연령"."연령", 
	    "2_구직취업현황_연령"."구직건수", 
	    "2_구직취업현황_연령"."취업건수" *-1 AS "취업건수"
    FROM
	    "인력수급현황"."2_구직취업현황_연령"
    WHERE
	    "2_구직취업현황_연령"."연도" = '{year}' AND
	    "2_구직취업현황_연령"."월" = '{month}'
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result 

def jobed_mid(db:Session,year:str,month:str):
    sql = f"""
    SELECT
	    "7.구인구직취업현황_직업분류"."연도", 
	    "7.구인구직취업현황_직업분류"."월", 
	    "7.구인구직취업현황_직업분류"."직종_중분류", 
	    SUM("7.구인구직취업현황_직업분류"."구인인원(월)") AS 구인인원합계, 
	    SUM("7.구인구직취업현황_직업분류"."구직건수(월)") AS 구직건수합계, 
	    SUM("7.구인구직취업현황_직업분류"."취업건수(월)") AS 취업건수합계
    FROM
	    "인력수급현황"."7.구인구직취업현황_직업분류"
    WHERE
	    "7.구인구직취업현황_직업분류"."연도" = '{year}' AND
	    "7.구인구직취업현황_직업분류"."월" = '{month}'
    GROUP BY
	    "7.구인구직취업현황_직업분류"."직종_중분류",
        "7.구인구직취업현황_직업분류"."연도", 
	    "7.구인구직취업현황_직업분류"."월"
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def jobed(db:Session,year:str,month:str):
    sql = f"""
    SELECT
	    "7.구인구직취업현황_직업분류"."직종_소분류", 
	    "7.구인구직취업현황_직업분류"."직종_중분류", 
	    "7.구인구직취업현황_직업분류"."연도", 
	    "7.구인구직취업현황_직업분류"."월", 
	    "7.구인구직취업현황_직업분류"."구인인원(월)", 
	    "7.구인구직취업현황_직업분류"."구직건수(월)", 
	    "7.구인구직취업현황_직업분류"."취업건수(월)"
    FROM
	    "인력수급현황"."7.구인구직취업현황_직업분류"
    WHERE
	    "7.구인구직취업현황_직업분류"."연도" = '{year}' AND
	    "7.구인구직취업현황_직업분류"."월" = '{month}'
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result 


def educationed(db:Session,year:str,month:str):
    sql = f"""
    SELECT
	    "3_구인구직취업현황_학력"."연도", 
	    "3_구인구직취업현황_학력"."월", 
	    "3_구인구직취업현황_학력"."학력", 
	    "3_구인구직취업현황_학력"."구인인원", 
	    "3_구인구직취업현황_학력"."구직건수", 
	    "3_구인구직취업현황_학력"."취업건수"
    FROM
	    "인력수급현황"."3_구인구직취업현황_학력"
    WHERE
	    "3_구인구직취업현황_학력"."연도" = '{year}' AND
	    "3_구인구직취업현황_학력"."월" = '{month}'
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result