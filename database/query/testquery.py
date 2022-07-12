from sqlalchemy.orm import Session

def workread(db: Session, legion: str, code: str):
    sql= f"""SELECT DISTINCT ROW_NUMBER() OVER ( ORDER BY "지역별" ) AS recid, *
 FROM "총괄_고용형태_지역" 
 WHERE "지역별" = '{legion}' AND "VAR1" = '{code}'
 ORDER BY recid """
    result = db.execute(sql)
    data = result.fetchall()
    return data