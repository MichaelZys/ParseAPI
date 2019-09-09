import psycopg2
import time
import psycopg2.extras
import os

# 如果不使用 psycopg2.extras 这种， 会导得到的数据时元祖， 而没有列名。
# execSqlFetchall 返回结果，类型<class 'list'> 其实是字典表， 里面都是<class 'psycopg2.extras.RealDictRow'>。
# logfile = os.path.dirname(os.path.dirname(os.getcwd())) + '\log\log.txt'


# print(logfile)


class dba(object):
    def __init__(self):
        self.host = '192.168.0.222'
        self.database = 'ocm'
        self.user = 'postgres'
        self.password = '@'
        self.application_name = 'api_sftm'

    # @classmethod
    def execsql(self, sql):
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cur = self.conn.cursor()
        try:
            # print(sql)
            cur.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            print(sql)
            # f = open(logfile, 'w')
            # f.writelines(sql)
            # f.close()
            raise (Exception)

        finally:
            cur.close()
            self.conn.close()

    def execSqlFetchone(self, sql):
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cur = self.conn.cursor()
        try:
            cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(sql)
            result = cur.fetchone()
            return result
        except Exception:

            self.conn.rollback()
            # print(Exception)
            print('异常sql语句:' + sql)
            raise (Exception)

        finally:
            cur.close()
            self.conn.close()

    def execSqlFetchall(self, sql):
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cur = self.conn.cursor()
        try:
            cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception:
            self.conn.rollback()
            # print(Exception)
            print('异常sql语句:' + sql)
            raise (Exception)

        finally:
            cur.close()
            self.conn.close()

    def insertMany(self, sql, list):
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cur = self.conn.cursor()
        try:
            cur.executemany(sql, list)
            self.conn.commit()
        except Exception:

            self.conn.rollback()
            # print(Exception)
            print('异常sql语句:' + sql)
            raise (Exception)

        finally:
            cur.close()
            self.conn.close()

    def execListSql(self, list):
        # t1 = time.time()
        str_sql = ''
        for _ in list:
            str_sql = str_sql + _
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cur = self.conn.cursor()
        try:
            cur.execute(str_sql)

            self.conn.commit()
        except Exception:
            self.conn.rollback()
            # print(Exception)
            # print('异常sql语句:' + str_sql)
            raise (Exception)

        finally:
            cur.close()
            self.conn.close()
            # print('耗時：')
            # print(time.time()-t1)
