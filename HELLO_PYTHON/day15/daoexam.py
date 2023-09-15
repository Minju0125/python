import pymysql

class DaoExam:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python',port=3305, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql=f"""
            select e_id, m_id, kor, eng, math from exam
            """
        self.curs.execute(sql)
        mylist= self.curs.fetchall()
        return mylist
    
    def selectOne(self, e_id):
        sql=f"""
            select
                e_id, m_id, kor, eng, math
            from 
                exam
            where e_id='{e_id}'
        """
        self.curs.execute(sql)
        mylist= self.curs.fetchall()
        return mylist[0]

    def __del__(self):
        self.curs.close()
        self.curs.close()
    
    def insert(self, m_id, kor, eng, math):
        sql=f"""
            insert into 
                exam (m_id, kor, eng, math) 
            values 
                ('{m_id}','{kor}','{eng}','{math}')
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, m_id, kor, eng, math):
        sql=f"""
                update
                    exam 
                set 
                    m_id='{m_id}',
                    kor='{kor}',
                    eng='{eng}',
                    math='{math}'
                where
                    e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql=f"""
                delete 
                    from exam 
                where
                    e_id='{e_id}'
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
if __name__ =='__main__':
    de = DaoExam()
    cnt = de.delete('1')
    print("cnt", cnt)