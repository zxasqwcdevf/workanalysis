from sqlalchemy.orm import Session

#dict 타입으로 반환
def work(db:Session):
    sql = f"""
    SELECT 
    FROM 
    WHERE 
    GROUP BY 
    ORDER BY
    """
    sql_result = db.execute(sql)
    data = sql_result.fetchall()
    result = [r._asdict() for r in data]
    return result