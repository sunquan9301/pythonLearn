import math


class DataPre:
    def __init__(self, data=[]):
        self.data = data

    def simDistance(self, persion1, persion2):
        # 越相似，结果越接近1
        si = {}
        for item in self.data[persion1]:
            if item in self.data[persion2]:
                si[item] = 1

        if len(si) == 0:
            return 0

        # 欧几里得相关系数，直接根据坐标计算点之间点相关距离
        sum_distance = sum(
            [pow(self.data[persion1][item] - self.data[persion2][item], 2) for item in self.data[persion1] if
             item in self.data[persion2]]
        )
        return 1 / (1 + math.sqrt(sum_distance))

    def topMatches(self, person, method,n=3):
        scores = [(method(person, other), other) for other in self.data if other != person]
        scores.sort()
        scores.reverse()
        return scores[0:n]

    def sim_pearson(self, p1, p2):
        # 皮尔逊相关度评价
        si = {}
        for item in self.data[p1]:
            if item in self.data[p2]:
                si[item] = 1

        n = len(si)
        if n == 0:
            return 1

        sum1 = sum([self.data[p1][it] for it in si])
        sum2 = sum([self.data[p2][it] for it in si])

        sum1Sq = sum([pow(self.data[p1][it], 2) for it in si])
        sum2Sq = sum([pow(self.data[p2][it], 2) for it in si])

        pSum = sum([self.data[p1][it] * self.data[p2][it] for it in si])

        num = pSum - (sum1 * sum2 / n)
        den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
        if den == 0: return 0
        return num / den
