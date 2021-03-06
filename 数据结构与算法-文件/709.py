class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.Discovery = None
        self.Finish = None
        self.color = 'while'
        self.pred = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo :' \
            + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDiscovery(self, time):
        self.Discovery = time

    def setFinish(self, time):
        self.Finish = time

    def setColor(self, col):
        self.color = col

    def getColor(self):
        return self.color

    def setPred(self, vertex):
        self.pred = vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class DFGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor("while")
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == "while":
                self.dfsvisit(aVertex)

    def dfsvisit(self, srartVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'while':
                nextVertex.setPred(satartVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)
