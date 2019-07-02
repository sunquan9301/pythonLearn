import feedparser
from clustering.DataUtil import DataUtil


def main():
    feedlist = DataUtil.getItemList("feedlists")
    for url in feedlist:
        DataUtil.getWordCounts(url.strip())


if __name__ == "__main__":
    main()
