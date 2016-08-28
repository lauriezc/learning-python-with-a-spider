# lauriezc
# 2016-08-24 21:28:28
# spider data access
import MySQLdb


class SpiderDB(object):
    def __init__(self,con
    def testdb(self):
        con = MySQLdb.connect(host='localhost', user='root',
                              passwd='mn', db='cms', port=3306)
        cur = con.cursor()
        cur.execute('SELECT * FROM cms_articles')
        rs = cur.fetchall()
        for r in rs:
            print r
        cur.close()
        con.close()
