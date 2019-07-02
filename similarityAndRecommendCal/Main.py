from similarityAndRecommendCal.data.Recommendations import critics
from similarityAndRecommendCal.data.DataPre import DataPre
"""
    1.相似度计算，定义了欧拉距离和皮尔森距离来做物品相似度推荐 dataPre.topMatches
    2.推荐电影 dataPre.recommendMovies, 选择不同的推荐算法对结果影响甚微
"""


def main():
    dataPre = DataPre(critics)
    print(dataPre.topMatches("Lisa Rose", dataPre.sim_pearson, 3))
    # print(dataPre.topMatches("Lisa Rose", dataPre.sim_pearson, 3))
    print(dataPre.getRecommends("Toby", dataPre.sim_pearson))
    print(dataPre.getRecommends("Toby", dataPre.simDistance))
    # add(addOne, [1, 2, 3])

    print("=======transform data=======")
    dataPrePerson = DataPre(transformData(critics))
    # print(dataPrePerson.topMatches("Superman Returns", dataPrePerson.sim_pearson, 3))
    print(dataPrePerson.getRecommends("Just My Luck", dataPrePerson.simDistance))
    print(dataPrePerson.getRecommends("Just My Luck", dataPrePerson.sim_pearson))


def transformData(data):
    result = {}
    for person in data:
        for item in data[person]:
            result.setdefault(item, {})
            result[item][person] = data[person][item]
    return result


def add(method, value=[]):
    for v in value:
        method(v)


def addOne(v):
    v += 1
    print(v)


if __name__ == "__main__":
    main()
