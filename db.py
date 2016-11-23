# lauriezc
# 2016-08-24 21:28:28
# spider data access
import MySQLdb


class spider_db(object):
    def __init__(self, host, uid, pwd, db, port):
        self._host = host
        self._uid = uid
        self._pwd = pwd
        self._db = db
        self._port = port

    def Connect(self):
        return MySQLdb.connect(host=self._host, user=self._uid,
                               passwd=self._pwd, db=self._db, port=self._port)

    def Query(self, sql):
        con = self.Connect()
        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        con.close()
        return result

    def Execute(self, sql, param):
        con = self.Connect()
        cur = con.cursor()
        n = cur.execute(sql, param)
        cur.close()
        con.commit()
        con.close()
        return n
