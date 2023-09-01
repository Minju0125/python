import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql="""
    insert into emp (e_id, e_name, gen, addr) 
    values (%s,%s,%s,%s)
"""
curs.execute(sql, ('3','3','3''3'))

conn.commit()

curs.close()
conn.close()