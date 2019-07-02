import clustering.DataPreUtil as DataPreUtil
import clustering.Config as config


class Clusters:

    def startCluster(self):
        rownames, colnames, data = self.readFile(config.outputName)
        self.hcluster(data)

    def readFile(self, fileName):
        lines = []
        try:
            with open(fileName) as f:
                lines = f.readlines()
        except BaseException:
            print("you encounter an Exception %s" % str(BaseException.args))

        colnames = lines[0].strip().split('\t')[1:]
        rownames = []
        data = []
        for line in lines[1:]:
            p = line.strip().split('\t')
            rownames.append(p[0])
            data.append([float(x) for x in p[1:]])
        return rownames, colnames, data

    def hcluster(self, rows, method=DataPreUtil.DataUtil.pearson):
        distances = {}
        currentClustid = -1
        clust = [bicluster(rows[i], id=i) for i in range(len(rows))]

        while len(clust) > 1:
            lowestPair = (0, 1)
            closest = method(clust[0].vec, clust[1].vec)

            for i in range(len(clust)):
                for j in range(i + 1, len(clust)):

                    if (clust[i].id, clust[j].id) not in distances:
                        distances[(clust[i].id, clust[j].id)] = method(clust[i].vec, clust[j].vec)
                        d = distances[(clust[i].id, clust[j].id)]
                        if d < closest:
                            closest = d
                            lowestPair = (i, j)

            mergeVec = [(clust[lowestPair[0]].vec[i] + clust[lowestPair[1]].vec[i]) / 2.0 for i in
                        range(len(clust[0].vec))]
            newCluster = bicluster(mergeVec, left=clust[lowestPair[0]], right=clust[lowestPair[1]], distance=closest,
                                   id=currentClustid)
            # 不在原始集合中的聚类，其 id 为负盛t
            currentClustid -= 1
            print("this round cluster %d and cluster %d is clostest" % (lowestPair[0], lowestPair[1]))
            del clust[lowestPair[1]]
            del clust[lowestPair[0]]
            clust.append(newCluster)

        return clust[0]


class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance
