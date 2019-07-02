import feedparser
import re
import ssl
import clustering.Config as config
import math


class DataUtil:
    @staticmethod
    def pearson(v1, v2):
        sum1 = sum(v1)
        sum2 = sum(v2)

        sum1Sq = sum([pow(v, 2) for v in v1])
        sum2Sq = sum([pow(v, 2) for v in v2])

        pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

        num = pSum - (sum1 * sum2 / len(v1))
        den = math.sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
        if den == 0: return 0

        return 1.0 - num / den

    @staticmethod
    def startPreData():
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        feedlist = DataUtil.getItemList(config.inputName)
        appcount = {}
        wordcounts = {}
        for url in feedlist:
            title, wc = DataUtil.getWordCounts(url.strip())
            wordcounts[title] = wc
            for word, count in wc.items():
                appcount.setdefault(word, 0)
                if count > 1:
                    appcount[word] += 1
        print(appcount)
        print(wordcounts)
        wordlist = []
        for w, bc in appcount.items():
            frac = float(bc) / len(feedlist)
            if (frac > 0.1 and frac < 0.5): wordlist.append(w)

        print(wordlist)

        try:
            with open(config.outputName, 'w') as out:
                out.write('Blog')
                for word in wordlist:
                    out.write('\t%s' % word)
                out.write('\n')
                for blog, wc in wordcounts.items():
                    out.write(blog)
                    for word in wordlist:
                        if word in wc:
                            out.write('\t%d' % wc[word])
                        else:
                            out.write('\t0')
                    out.write('\n')
        except Exception:
            print("you encounter an exception")

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
    def getWords(html):
        txt = re.compile(r'<[^>]+>').sub('', html)

        words = re.compile(r'[^A-Z^a-z]+').split(txt)

        return [word.lower() for word in words if word != '']

    @staticmethod
    def getWordCounts(url):
        print(url)
        d = feedparser.parse(url)
        wc = {}
        for e in d['entries']:
            if 'summary' in e:
                summary = e['summary']
            else:
                summary = e['description']
            words = DataUtil.getWords(e['title'] + '' + summary)
            for word in words:
                wc.setdefault(word, 0)
                wc[word] += 1
        return d['feed']['title'], wc
