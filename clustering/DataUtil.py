import feedparser
import ssl

class DataUtil:
    @staticmethod
    def getItemList(name):
        try:
            with open(name) as f:
                items = f.readlines()
                result = [item.strip() for item in items]
                return result
        except Exception:
            print("you encounter an exception")
            return []

    @staticmethod
    def getWordCounts(url):
        print(url)
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        d = feedparser.parse(url)
        print(d)
