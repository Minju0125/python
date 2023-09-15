import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

e_id='6'
e_name='7'
gen='7'
addr='7'
curs = conn.cursor()

sql=f"""
    update emp 
    set 
        e_name='{e_name}',
        gen='{gen}',
        addr='{addr}'
    wherea
        e_id='{e_id}'
"""
cnt = curs.execute(sql)
print("cnt", cnt)
print("cnt", curs.rowcount)
conn.commit()

curs.close()
conn.close()