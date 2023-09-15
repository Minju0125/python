import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from emp"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

#cursor => conn   
 
curs.close()
conn.close()