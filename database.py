'''
@Author: YuleZhang
@Description: 
@Date: 2020-04-02 09:28:49
'''
import pymysql

class Database():
    def __init__(self):
        host = 'localhost' #Host
        user = 'root' #Username
        password = '' #password
        db = 'financial_data' #Database Name
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def search_user(self):
        self.cur.execute("select * from login")
        result = self.cur.fetchall()
        return result

    def search_user_name(self,name):
        self.cur.execute("selec * from login where username = '"+name + "'")
        result = self.cur.fetchall()
        return result
    
    def insert_user(self,user,password):
        # print("insert into login values('"+user + "','"+password+"')")
        self.cur.execute("insert into login values(NULL,'"+user + "','"+password+"','普通用户')")
        self.con.commit()

    def delete_user(self,user):
        self.cur.execute("delete from login where loginUser = '"+user+"' and loginLevel = '普通用户'")
        self.con.commit()

    def modify_user(self,user,password):
        self.cur.execute("UPDATE login SET loginPass = '"+password+"' WHERE loginUser = '"+user+"'")
        self.con.commit()

    def improve_user(self,user):
        self.cur.execute("UPDATE login SET loginLevel = '管理员' WHERE loginUser = '"+user+"'")

    def search_file(self):
        self.cur.execute("select * from file")
        result = self.cur.fetchall()
        return result

    def search_file_cond(self,fileType,year):
        self.cur.execute("select * from file where fileType='"+fileType+"'and fileDate = '"+year+"'")
        result = self.cur.fetchall()
        return result
    # def insert_login(self,record):
    #     # ��login���в���һ����¼
    #     sql = "insert into login values(NULL,'" + "','".join(record) +"',0);"
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #     print('����ɹ�')
    #     pass

    # def insert_searchHis(self,record):
    #     # �������ʷ��¼���в���һ����¼
    #     sql = "insert into history values(NULL,'" + "','".join(record) +"');"
    #     print(sql)
    #     self.cursor.execute(sql)
    #     self.conn.commit()

    # def search(self,col,val):
    #     # �����û���Ϣ�����ز��ҽ���б����б���ÿ��Ԫ�ض���Ԫ��
    #     sql = ""
    #     if val == "":
    #         sql = "select * from login"
    #     else:
    #         sql = "select * from login where "+col+" = '" + str(val) + "'"
    #     self.cursor.execute(sql)
    #     rs = self.cursor.fetchall()
    #     return rs
    
    # def search_history(self):
    #     # �����û���Ϣ�����ز��ҽ���б����б���ÿ��Ԫ�ض���Ԫ��
    #     sql = "select * from history"
    #     self.cursor.execute(sql)
    #     rs = self.cursor.fetchall()
    #     return rs
    
    # def clearTable(self):
    #     # �����ʷ��
    #     sql = 'truncate table history;'
    #     self.cursor.execute(sql)
    #     self.conn.commit()

    # def update_search_time(self,user_id):
    #     sql = "update login set searchTimes = searchTimes + 1 where id = '"+str(user_id)+"'"
    #     self.cursor.execute(sql)
    #     self.conn.commit()

    # def __del__(self):
    #     self.cursor.close()
    #     self.conn.close()