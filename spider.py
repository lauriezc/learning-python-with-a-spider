# lauriezc
# 2016-08-23 20:25:23
# website spider
import urllib2


class spider(object):
    def take(self, uri):
        response = urllib2.urlopen(uri)
        print response.read()
s = spider()
s.take('http://www.baidu.com')
