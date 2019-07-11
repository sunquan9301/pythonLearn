import re
from urllib import request, parse
from bs4 import *
import sqlite3
import ssl


class Crawler:
    def __init__(self, dbname):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        self.con = sqlite3.connect(dbname)
        self.ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])

    def __del__(self):
        self.con.close()

    def dbcommit(self):
        self.con.commit()

    def createIndexTables(self):
        self.con.execute('create table url_list(url)')
        self.con.execute('create table word_list(word)')
        self.con.execute('create table word_location(urlid,wordid,location)')
        self.con.execute('create table link(fromid integer,toid integer)')
        self.con.execute('create table link_words(wordid,linkid)')
        self.con.execute('create index wordidx on word_list(word)')
        self.con.execute('create index urlidx on url_list(url)')
        self.con.execute('create index wordurlidx on word_location(wordid)')
        self.con.execute('create index urltoidx on link(toid)')
        self.con.execute('create index urlfromidx on link(fromid)')

    # 获取条目的id,如果条目不存在，就将其加入数据库中
    def getentryid(self, table, field, value, createnew=True):
        cur = self.con.execute("select rowid from %s where %s='%s'" % (table, field, value))
        res = cur.fetchone()
        if res == None:
            cur = self.con.execute("insert into %s (%s) values ('%s')" % (table, field, value))
            return cur.lastrowid
        else:
            return res[0]

    # 为每个网页建立索引
    def addtoindex(self, url, soup):
        if self.isindexed(url): return
        print('Indexing %s' % url)

        text = self.gettextonly(soup)
        words = self.separatewords(text)

        urlid = self.getentryid('urllist', 'url', url)

        for i in range(len(words)):
            word = words[i]
            if word in self.ignorewords: continue
            wordid = self.getentryid('wordlist', 'word', word)
            self.con.execute(
                "insert into word_location(urlid,wordid,location) values (%d,%d,%d)" % (urlid, wordid, i))

    # 从一个HTML网页中提取文字
    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c = soup.content
            resulttext = ""
            for t in c:
                subtext = self.gettextonly(t)
                resulttext += subtext + '\n'
            return resulttext
        else:
            return v.strip()

    # 根据任何非空白字符进行分词处理
    """
    只是简单的将任何非字母或非数字的字符作为分隔符
    
    """

    def separatewords(self, text):
        splitter = re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s != '']

    # 如果url已经建立索引，则返回true
    def isindexed(self, url):
        u = self.con.execute("select rowid from urllist where url = '%s'" % url).fetchone()
        if u != None:
            v = self.con.execute('select * from word_location where urlid=%d' % u[0]).fetchone()
            if v != None: return True
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
