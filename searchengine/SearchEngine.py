from urllib import request, parse
from bs4 import *
import ssl


class Crawler:
    def __init__(self, dbname):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

    def __del__(self):

        pass

    def dbcommit(self):
        pass

    # 获取条目的id,如果条目不存在，就将其加入数据库中
    def getentryid(self, table, field, value, createnew=True):
        return None

    # 为每个网页建立索引
    def addtoindex(self, url, soup):
        print('Indexing %s' % url)

    # 从一个HTML网页中提取文字
    def gettextonly(self, soup):
        return None

    # 根据任何非空白字符进行分词处理
    def separatewords(self, text):
        return None

    # 如果url已经建立索引，则返回true
    def isindexed(self, url):
        return False

    # 添加一个关联两个网页的链接
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    # 从一小组网页开始进行广度优先搜索，直至某一给定深度
    # 期间为网页建立索引
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = request.urlopen(page)
                except Exception as e:
                    print("Could not open %s" % page)
                    print("error msg is ", e.args)
                    continue
                soup = BeautifulSoup(c.read(), "html.parser")
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = parse.urljoin(page, link['href'])
                        if url.find("'") != -1: continue
                        url = url.split('#')[0]
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)
                self.dbcommit()
            pages = newpages

        print("end")

    # 创建数据库表
    def createindextables(self):
        pass
