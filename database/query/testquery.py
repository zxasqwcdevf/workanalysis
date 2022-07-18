from sqlalchemy.orm import Session

#list 타입으로 반환
def test1(db:Session):
    sql = f"""
    SELECT
	    "구인구직취업현황_근무지역"."시도", 
	    "구인구직취업현황_근무지역"."시군구", 
	    SUM("구인구직취업현황_근무지역"."구인인원") AS 구인인원합계, 
	    SUM("구인구직취업현황_근무지역"."구직건수" * -1) AS 구직건수합계, 
	    SUM("구인구직취업현황_근무지역"."취업건수") AS 취업건수합계
    FROM
	    "인력수급현황"."구인구직취업현황_근무지역"
    GROUP BY
	    "구인구직취업현황_근무지역"."시도", 
	    "구인구직취업현황_근무지역"."시군구"
    ORDER BY
	    "구인구직취업현황_근무지역"."시도" ASC, 
	    "구인구직취업현황_근무지역"."시군구" ASC
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result