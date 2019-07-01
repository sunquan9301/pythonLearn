from similarityCal.data.Recommendations import critics
from similarityCal.data.DataPre import DataPre

"""
    相似度计算，定义了欧拉距离和皮尔森距离来做物品相似度推荐
"""
def main():
    dataPre = DataPre(critics)
    print(dataPre.topMatches("Lisa Rose", dataPre.sim_pearson, 3))
    add(addOne, [1, 2, 3])


def add(method, value=[]):
    for v in value:
        method(v)


def addOne(v):
    v += 1
    print(v)


if __name__ == "__main__":
    main()
