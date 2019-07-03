import clustering.DataPreUtil as DataPreUtil
import clustering.Config as config
from PIL import Image, ImageDraw


class Clusters:

    def startCluster(self):
        blognames, words, data = self.readFile(config.outputName)
        clust = self.hcluster(data)
        # self.printclust(clust, labels=blognames)
        self.drawdendrogram(clust, blognames, jpeg='blogclust.jpg')

    def getHeight(self, clust):
        if clust.left == None and clust.right == None:
            return 1
        return self.getHeight(clust.left) + self.getHeight(clust.right)

    def getDepth(self, clust):
        if clust.left == None and clust.right == None: return 0
        return max(self.getDepth(clust.left), self.getDepth(clust.right)) + clust.distance

    def drawdendrogram(self, clust, labels, jpeg='clusters.jpg'):
        h = self.getHeight(clust) * 20
        w = 1200
        depth = self.getDepth(clust)

        scaling = float(w - 150) / depth
        print(h, w, depth, scaling)
        img = Image.new('RGB', (w, h), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.line((0, h / 2, 10, h / 2), fill=(255, 0, 0))
        self.drawnode(draw, clust, 10, (h / 2), scaling, labels)
        img.save(jpeg, 'JPEG')

    def drawnode(self, draw, clust, x, y, scaling, labels):
        if clust.id < 0:
            h1 = self.getHeight(clust.left) * 20
            h2 = self.getHeight(clust.right) * 20
            print("h1 = %r; h2 = %r, y = %r" % (h1, h2, y))
            top = y - (h1 + h2) / 2
            bottom = y + (h1 + h2) / 2
            print("top = %r; bottom = %r" % (top, bottom))
            # 线的长度
            l1 = clust.distance * scaling
            # 垂直线
            draw.line((x, top + h1 / 2, x, bottom - h2 / 2), fill=(255, 0, 0))
            # 链接到左侧节点到水平线
            draw.line((x, top + h1 / 2, x + l1, top + h1 / 2), fill=(255, 0, 0))
            # 链接到右侧节点到水平线
            draw.line((x, bottom - h2 / 2, x + l1, bottom - h2 / 2), fill=(255, 0, 0))

            self.drawnode(draw, clust.left, x + l1, top + h1 / 2, scaling, labels)
            self.drawnode(draw, clust.right, x + l1, bottom - h2 / 2, scaling, labels)
        else:
            draw.text((x + 5, y - 7), labels[clust.id].encode('latin-1','ignore'), (0, 0, 0))

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

    def printclust(self, clust, labels=None, n=0):
        str = ''

        for i in range(n):
            str = str + " "
        print(str, '-' if clust.id < 0 else clust.id)
        if clust.left != None: self.printclust(clust.left, labels=labels, n=n + 1)
        if clust.right != None: self.printclust(clust.right, labels=labels, n=n + 1)

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
