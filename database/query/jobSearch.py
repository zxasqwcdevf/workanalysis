from sqlalchemy.orm import Session

def employed(db:Session ,year:str, month:str):
    sql = f"""
   SELECT
        CASE
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 없는 근로계약'::text THEN 1
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 없는 근로계약(시간(선택)제)'::text THEN 2
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 있는 근로계약'::text THEN 3
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 있는 근로계약(시간(선택)제)'::text THEN 4
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '일용직'::text THEN 5
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '관계없음'::text THEN 6
            ELSE NULL::integer
        END AS code,
    "구인구직취업현황_고용형태"."연도",
    "구인구직취업현황_고용형태"."월",
    "구인구직취업현황_고용형태"."고용형태",
    "구인구직취업현황_고용형태"."구인인원",
    "구인구직취업현황_고용형태"."구직건수",
    "구인구직취업현황_고용형태"."취업건수"
   FROM "인력수급현황"."구인구직취업현황_고용형태"
  WHERE "구인구직취업현황_고용형태"."연도"::text = '{year}'::text AND "구인구직취업현황_고용형태"."월"::text = '{month}'::text
  ORDER BY (
        CASE
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 없는 근로계약'::text THEN 1
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 없는 근로계약(시간(선택)제)'::text THEN 2
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 있는 근로계약'::text THEN 3
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '기간의 정함이 있는 근로계약(시간(선택)제)'::text THEN 4
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '일용직'::text THEN 5
            WHEN "구인구직취업현황_고용형태"."고용형태"::text = '관계없음'::text THEN 6
            ELSE NULL::integer
        END)
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def industried(db:Session, year:str, month:str):
    sql = f"""
     SELECT
        CASE
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '농업, 임업 및 어업'::text THEN 1
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '광업'::text THEN 2
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '제조업'::text THEN 3
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '전기, 가스, 증기 및 공기조절 공급업'::text THEN 4
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '수도, 하수 및 폐기물 처리, 원료 재생업'::text THEN 5
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '건설업'::text THEN 6
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '도매 및 소매업'::text THEN 7
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '운수 및 창고업'::text THEN 8
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '숙박 및 음식점업'::text THEN 9
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '정보통신업'::text THEN 10
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '금융 및 보험업'::text THEN 11
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '부동산업'::text THEN 12
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '전문, 과학 및 기술 서비스업'::text THEN 13
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '사업시설 관리, 사업 지원 및 임대 서비스업'::text THEN 14
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '공공행정, 국방 및 사회보장 행정'::text THEN 15
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '교육 서비스업'::text THEN 16
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '보건업 및 사회복지 서비스업'::text THEN 17
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '예술, 스포츠 및 여가관련 서비스업'::text THEN 18
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '협회 및 단체, 수리 및 기타 개인 서비스업'::text THEN 19
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '가구 내 고용활동 및 달리 분류되지 않은 자가소비 생산활동'::text THEN 20
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '국제 및 외국기관'::text THEN 21
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '분류불능'::text THEN 22
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '해당없음'::text THEN 23
            ELSE NULL::integer
        END AS code,
    "구인구직취업현황_산업분류"."연도",
    "구인구직취업현황_산업분류"."월",
    "구인구직취업현황_산업분류"."산업_대분류",
    "구인구직취업현황_산업분류"."구인인원(월)",
    "구인구직취업현황_산업분류"."취업건수(월)" * -1 AS "취업건수(월)"
   FROM "인력수급현황"."구인구직취업현황_산업분류"
  WHERE "구인구직취업현황_산업분류"."연도"::text = '{year}'::text AND "구인구직취업현황_산업분류"."월"::text = '{month}'::text
  ORDER BY (
        CASE
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '농업, 임업 및 어업'::text THEN 1
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '광업'::text THEN 2
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '제조업'::text THEN 3
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '전기, 가스, 증기 및 공기조절 공급업'::text THEN 4
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '수도, 하수 및 폐기물 처리, 원료 재생업'::text THEN 5
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '건설업'::text THEN 6
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '도매 및 소매업'::text THEN 7
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '운수 및 창고업'::text THEN 8
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '숙박 및 음식점업'::text THEN 9
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '정보통신업'::text THEN 10
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '금융 및 보험업'::text THEN 11
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '부동산업'::text THEN 12
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '전문, 과학 및 기술 서비스업'::text THEN 13
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '사업시설 관리, 사업 지원 및 임대 서비스업'::text THEN 14
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '공공행정, 국방 및 사회보장 행정'::text THEN 15
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '교육 서비스업'::text THEN 16
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '보건업 및 사회복지 서비스업'::text THEN 17
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '예술, 스포츠 및 여가관련 서비스업'::text THEN 18
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '협회 및 단체, 수리 및 기타 개인 서비스업'::text THEN 19
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '가구 내 고용활동 및 달리 분류되지 않은 자가소비 생산활동'::text THEN 20
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '국제 및 외국기관'::text THEN 21
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '분류불능'::text THEN 22
            WHEN "구인구직취업현황_산업분류"."산업_대분류"::text = '해당없음'::text THEN 23
            ELSE NULL::integer
        END)
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def gendered(db:Session,year:str, month:str):
    sql = f"""
     SELECT
        CASE
            WHEN "구인구직취업현황_성별"."성별"::text = '남'::text THEN 1
            WHEN "구인구직취업현황_성별"."성별"::text = '여'::text THEN 2
            WHEN "구인구직취업현황_성별"."성별"::text = '무관'::text THEN 3
            ELSE NULL::integer
        END AS code,
    "구인구직취업현황_성별"."연도",
    "구인구직취업현황_성별"."월",
    "구인구직취업현황_성별"."성별",
    "구인구직취업현황_성별"."구직건수",
    "구인구직취업현황_성별"."취업건수" *-1 AS "취업건수"
   FROM "인력수급현황"."구인구직취업현황_성별"
    WHERE "구인구직취업현황_성별"."연도"::text = '{year}'::text AND "구인구직취업현황_성별"."월"::text = '{month}'::text
    ORDER BY (
        CASE
            WHEN "구인구직취업현황_성별"."성별"::text = '남'::text THEN 1
            WHEN "구인구직취업현황_성별"."성별"::text = '여'::text THEN 2
            WHEN "구인구직취업현황_성별"."성별"::text = '무관'::text THEN 3
            ELSE NULL::integer
        END)
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def aged(db:Session,year:str,month:str):
    sql = f"""
    SELECT
        CASE
            WHEN "구인구직취업현황_연령"."연령"::text = '19세이하'::text THEN 1
            WHEN "구인구직취업현황_연령"."연령"::text = '20~24세'::text THEN 2
            WHEN "구인구직취업현황_연령"."연령"::text = '25~29세'::text THEN 3
            WHEN "구인구직취업현황_연령"."연령"::text = '30~34세'::text THEN 4
            WHEN "구인구직취업현황_연령"."연령"::text = '35~39세'::text THEN 5
            WHEN "구인구직취업현황_연령"."연령"::text = '40~44세'::text THEN 6
            WHEN "구인구직취업현황_연령"."연령"::text = '45~49세'::text THEN 7
            WHEN "구인구직취업현황_연령"."연령"::text = '50~54세'::text THEN 8
            WHEN "구인구직취업현황_연령"."연령"::text = '55~59세'::text THEN 9
            WHEN "구인구직취업현황_연령"."연령"::text = '60~64세'::text THEN 10
            WHEN "구인구직취업현황_연령"."연령"::text = '65세이상'::text THEN 11
            WHEN "구인구직취업현황_연령"."연령"::text = '무관'::text THEN 12
            ELSE NULL::integer
        END AS code,
    "구인구직취업현황_연령"."연도",
    "구인구직취업현황_연령"."월",
    "구인구직취업현황_연령"."연령",
    "구인구직취업현황_연령"."구직건수",
    "구인구직취업현황_연령"."취업건수" *-1 AS "취업건수"
   FROM "인력수급현황"."구인구직취업현황_연령"
  WHERE "구인구직취업현황_연령"."연도"::text = '{year}'::text AND "구인구직취업현황_연령"."월"::text = '{month}'::text
  ORDER BY (
        CASE
            WHEN "구인구직취업현황_연령"."연령"::text = '19세이하'::text THEN 1
            WHEN "구인구직취업현황_연령"."연령"::text = '20~24세'::text THEN 2
            WHEN "구인구직취업현황_연령"."연령"::text = '25~29세'::text THEN 3
            WHEN "구인구직취업현황_연령"."연령"::text = '30~34세'::text THEN 4
            WHEN "구인구직취업현황_연령"."연령"::text = '35~39세'::text THEN 5
            WHEN "구인구직취업현황_연령"."연령"::text = '40~44세'::text THEN 6
            WHEN "구인구직취업현황_연령"."연령"::text = '45~49세'::text THEN 7
            WHEN "구인구직취업현황_연령"."연령"::text = '50~54세'::text THEN 8
            WHEN "구인구직취업현황_연령"."연령"::text = '55~59세'::text THEN 9
            WHEN "구인구직취업현황_연령"."연령"::text = '60~64세'::text THEN 10
            WHEN "구인구직취업현황_연령"."연령"::text = '65세이상'::text THEN 11
            WHEN "구인구직취업현황_연령"."연령"::text = '무관'::text THEN 12
            ELSE NULL::integer
        END)
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result 

def jobed_mid(db:Session,year:str,month:str):
    sql = f"""
     SELECT
	    "구인구직취업현황_직업분류"."연도", 
	    "구인구직취업현황_직업분류"."월", 
	    "구인구직취업현황_직업분류"."직종_중분류", 
	    SUM("구인구직취업현황_직업분류"."구인인원(월)") AS 구인인원합계, 
	    SUM("구인구직취업현황_직업분류"."구직건수(월)") AS 구직건수합계, 
	    SUM("구인구직취업현황_직업분류"."취업건수(월)") AS 취업건수합계
    FROM
	"인력수급현황"."구인구직취업현황_직업분류"
	JOIN
	    "인력수급현황"."직업_CODE"
	        ON 
		"구인구직취업현황_직업분류"."직종_중분류"::text = "인력수급현황"."직업_CODE"."중분류"::text
    WHERE
	    "구인구직취업현황_직업분류"."연도"::text = '{year}'::text AND
	    "구인구직취업현황_직업분류"."월"::text = '{month}'::text
    GROUP BY
	    "구인구직취업현황_직업분류"."직종_중분류", 
	    "구인구직취업현황_직업분류"."연도", 
	    "구인구직취업현황_직업분류"."월", 
	    "인력수급현황"."직업_CODE"."CODE_ID"
    ORDER BY
	    "인력수급현황"."직업_CODE"."CODE_ID" ASC
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result

def jobed(db:Session,year:str,month:str):
    sql = f"""
    SELECT 
    "구인구직취업현황_직업분류"."연도",
    "구인구직취업현황_직업분류"."월",
    "구인구직취업현황_직업분류"."직종_중분류",
    "구인구직취업현황_직업분류"."직종_소분류",
    "구인구직취업현황_직업분류"."구인인원(월)",
    "구인구직취업현황_직업분류"."구직건수(월)",
    "구인구직취업현황_직업분류"."취업건수(월)"
   FROM "인력수급현황"."구인구직취업현황_직업분류"
     JOIN "인력수급현황"."직업_CODE" ON "구인구직취업현황_직업분류"."직종_중분류"::text = "직업_CODE"."중분류"::text
  WHERE "구인구직취업현황_직업분류"."연도"::text = '{year}'::text AND "구인구직취업현황_직업분류"."월"::text = '{month}'::text
  ORDER BY "직업_CODE"."CODE_ID"
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result 


def educationed(db:Session,year:str,month:str):
    sql = f"""
    SELECT
        CASE
            WHEN "구인구직취업현황_학력"."학력"::text = '초졸'::text THEN 1
            WHEN "구인구직취업현황_학력"."학력"::text = '중졸'::text THEN 2
            WHEN "구인구직취업현황_학력"."학력"::text = '고졸'::text THEN 3
            WHEN "구인구직취업현황_학력"."학력"::text = '전문대졸'::text THEN 4
            WHEN "구인구직취업현황_학력"."학력"::text = '대졸'::text THEN 5
            WHEN "구인구직취업현황_학력"."학력"::text = '대학원졸(석사)'::text THEN 6
            WHEN "구인구직취업현황_학력"."학력"::text = '대학원졸(박사)'::text THEN 7
            WHEN "구인구직취업현황_학력"."학력"::text = '학력무관'::text THEN 8
            WHEN "구인구직취업현황_학력"."학력"::text = '분류불능'::text THEN 9
            ELSE NULL::integer
        END AS code,
    "구인구직취업현황_학력"."연도",
    "구인구직취업현황_학력"."월",
    "구인구직취업현황_학력"."학력",
    "구인구직취업현황_학력"."구인인원",
    "구인구직취업현황_학력"."구직건수",
    "구인구직취업현황_학력"."취업건수"
   FROM "인력수급현황"."구인구직취업현황_학력"
  WHERE "구인구직취업현황_학력"."연도"::text = '{year}'::text AND "구인구직취업현황_학력"."월"::text = '{month}'::text
  ORDER BY (
        CASE
            WHEN "구인구직취업현황_학력"."학력"::text = '초졸'::text THEN 1
            WHEN "구인구직취업현황_학력"."학력"::text = '중졸'::text THEN 2
            WHEN "구인구직취업현황_학력"."학력"::text = '고졸'::text THEN 3
            WHEN "구인구직취업현황_학력"."학력"::text = '전문대졸'::text THEN 4
            WHEN "구인구직취업현황_학력"."학력"::text = '대졸'::text THEN 5
            WHEN "구인구직취업현황_학력"."학력"::text = '대학원졸(석사)'::text THEN 6
            WHEN "구인구직취업현황_학력"."학력"::text = '대학원졸(박사)'::text THEN 7
            WHEN "구인구직취업현황_학력"."학력"::text = '학력무관'::text THEN 8
            WHEN "구인구직취업현황_학력"."학력"::text = '분류불능'::text THEN 9
            ELSE NULL::integer
        END)
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result