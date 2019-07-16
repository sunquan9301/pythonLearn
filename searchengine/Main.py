from searchengine.SearchEngine import Crawler
from urllib import request, error, parse, robotparser, response


def main():
    pagelist = ['https://www.huxiu.com/']
    crawler = Crawler('searchindex.db')
    crawler.createIndexTables()
    crawler.crawl(pagelist)

    # c = request.urlopen('http://www.hao123.com/')
    # contents = c.read()
    # print(contents)


if (__name__ == "__main__"):
    main()
