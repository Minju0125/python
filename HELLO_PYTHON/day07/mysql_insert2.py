import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id='4'
e_name='4'
gen='4'
addr='4'
curs = conn.cursor()

sql=f"""
    insert into emp (e_id, e_name, gen, addr) 
    values ('{e_id}','{e_name}','{gen}','{addr}')
"""
curs.execute(sql)
conn.commit()

curs.close()
conn.close()