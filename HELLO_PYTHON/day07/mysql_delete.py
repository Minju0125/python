import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id='6'

curs = conn.cursor()

sql=f"""
    delete 
    from emp 
    where
        e_id='{e_id}'
"""
cnt = curs.execute(sql)
print("cnt", cnt)
conn.commit()

curs.close()
conn.close()