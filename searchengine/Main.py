from searchengine.SearchEngine import Crawler
from urllib import request, error, parse, robotparser, response


def main():
    pagelist = ['http://www.hao123.com/']
    crawler = Crawler('')
    # crawler.crawl(pagelist)
    crawler.createIndexTables()

    # c = request.urlopen('http://www.hao123.com/')
    # contents = c.read()
    # print(contents)


if (__name__ == "__main__"):
    main()
