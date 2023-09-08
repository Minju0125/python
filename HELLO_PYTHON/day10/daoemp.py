import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python',port=3305, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql="select * from emp"
        self.curs.execute(sql)
        mylist= self.curs.fetchall()
        return mylist

    def selectOne(self, e_id):
        sql=f"""
            select 
                e_id, e_name, gen, addr
            from 
                emp
            where e_id='{e_id}'
        """
        self.curs.execute(sql)
        mylist= self.curs.fetchall()
        return mylist[0] #배열로 가져오고, 데이터가 하나밖에 없으므로 0번재 배열

    def insert(self,e_id, e_name, gen, addr):
        sql=f"""
            insert into 
                emp (e_id, e_name, gen, addr) 
            values 
                ('{e_id}','{e_name}','{gen}','{addr}')
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql=f"""
                delete 
                    from emp 
                where
                    e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql=f"""
                update
                    emp 
                set 
                    e_name='{e_name}',
                    gen='{gen}',
                    addr='{addr}'
                where
                    e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt

    def __del__(self):
        self.curs.close()
        self.curs.close()
    
if __name__ =='__main__':
    de = DaoEmp()
    cnt = de.update('6', '1', '1', '1')
    print("cnt", cnt)