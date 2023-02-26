import pymysql
import tkinter.messagebox as mes

class db_func():
    def __init__ (self, host, user, passwd, name):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.name = name
        self.cur =  0
        print('\n')
        try:
            self.db = pymysql.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.name, port = 3306, charset ='utf8')
            self.cur = self.db.cursor()
            print('数据库连接成功!')
            self.ent = self.enter(True)
        except pymysql.Error as err:
            self.db = 0
            self.cur = 0
            print('数据库连接失败\n' + str(err))
            mes.showerror(title = '',message='数据库链接失败\n' + str(err))
            self.ent = self.enter(False)
            

    def grant (self, username, pswd):
        sql_query = 'create user \'' + str(username) + '\'\'@\'139.9.119.34\' identified by \'' + pswd + '\';'
        try:
            self.cur.execute(sql_query + ';')
            self.db.commit()
            print('注册成功!')
            return True
        except:
            print('注册失败!')
            return False

    def enter (self, is_enter):
        return is_enter


    def find_cols(self, tab_name):
        query = 'show columns from `'+str(tab_name) + '`'
        print(query)
        self.cur.execute(query + ';')
        cols = ''
        for col in self.cur.fetchall():
            cols += ',' + col[0]
        cols = cols[1:]
        return cols


    def insert (self, tab_name, values):
        cols = self.find_cols(tab_name)
        sql_query = 'insert into `' + str(tab_name) + '`(' + str(cols) + ') value' + str(values)
        print(sql_query)
        try:
            self.cur.execute(sql_query + ';')
            self.db.commit()
            print("insert succeeded!")
            self.cur.close()
            self.db.commit()
            self.cur = self.db.cursor()
            return True
        except pymysql.Error as e:
            print("insert failed:" + str(e) )
            self.db.rollback()
            self.cur.close()
            self.db.commit()
            self.cur = self.db.cursor()
            mes.showerror(title = '',message='插入失败\n' + str(e))
            return False


    def search(self, tab_name, eq_cols = [], values = [], tg_cols = '*', special_cond = [], conne = [], sep = '', order = ''):
        sql_query = 'select ' + str(tg_cols) + ' from `' + str(tab_name) + '`'
        if eq_cols != []:
            sql_query += ' where ('
            for i in range(len(eq_cols)):
                sql_query += '`' + str(eq_cols[i]) + '`'
                if special_cond[i] == 'equal' or  special_cond[i] == 'in':
                    sql_query += ' in (' + str(values[i]) + ')'
                elif special_cond[i] == 'bigger':
                    sql_query += ' > ' + str(values[i])
                elif special_cond[i] == 'smaller':
                    sql_query += ' < ' + str(values[i])
                elif special_cond[i] == 'not in':
                    sql_query += ' not in ' + str(values[i])
                if i < len(eq_cols)-1:
                    sql_query += ' ' + str(conne[i]) + ' '
        #res_dic = {}
            sql_query += ') ' + sep + ' '
        if order != '':
            sql_query += ' order by ' + order
        print(sql_query)
        cols = self.find_cols(tab_name)
        res = []
        res.append(cols)
        try:
            self.cur.execute(sql_query + ';')
            self.db.commit()
            #res = self.cur.fetchall()
            print("search succeeded!")
            #print(self.cur.fetchall())
            #print(res)
            while 1:
                res1 = self.cur.fetchone()
                if res1 is None:
                    # 表示已经取完结果集
                    break
                res.append(res1)
                #print(res)
        except pymysql.Error as e:
            print("search failed:" + str(e) )
            mes.showerror (title = '',message='查询失败\n' + str(e))
            self.db.rollback()
        self.cur.close()
        self.db.commit()
        self.cur = self.db.cursor()
        return res

    
    def del_row(self, tab_name, key_name, values):
        sql_query = 'delete from `' + str(tab_name) + '` where `' + str(key_name) + '` in (\'' + str(values) + '\')'
        print(sql_query)
        try:
            self.cur.execute(sql_query + ';')
            self.db.commit()
            self.cur.close()
            self.db.commit()
            self.cur = self.db.cursor()
            print("delete succeeded!\n")
            mes.showinfo(title = '',message='删除成功')
            return True
        except pymysql.Error as e:
            print("delete failed:" + str(e) )
            self.db.rollback()
            self.cur.close()
            self.db.commit()
            self.cur = self.db.cursor()
            mes.showerror(title = '',message='删除失败\n' + str(e))
            return False


    def alt_num(self, tab_name, tg_col, tg_value, key_cols = [], key_values = [], conne = []):
        sql_query = 'update `' + str(tab_name) +'` set `' + str(tg_col) + '` = \'' + str(tg_value) + '\''
        if key_cols != []:
            sql_query += ' where ('
            for i in range(len(key_cols)):
                sql_query += str(key_cols[i]) + ' = ' + '(' + str(key_values[i]) + ')'
                if i < len(conne):
                    sql_query += ' ' + str(conne[i]) + ' '
            sql_query += ')'
        print(sql_query)
        try:
            self.cur.execute(sql_query + ';')
            self.db.commit()
            print("update succeeded!")
            mes.showinfo (title = '',message='修改成功')
        except pymysql.Error as e:
            print("update failed:" + str(e) )
            mes.showerror (title = '',message='修改失败\n' + str(e))
            self.db.rollback()
        self.cur.close()
        self.db.commit()
        self.cur = self.db.cursor()
        