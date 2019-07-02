from clustering.DataPreUtil import DataUtil
from clustering.Clusters import Clusters

"""
A     B     C     D     E
  AB        C        DE
       ABC           DE
             ABCDE
分级聚类
树状图是分级聚类的一种可视化形式

由于博客数据的量是不一样的，有的文章多，有的文章少，
所以这里用pearson距离来进行衡量
"""


def main():
    DataUtil.startPreData()
    clusters = Clusters()
    clusters.startCluster()

if __name__ == "__main__":
    main()
