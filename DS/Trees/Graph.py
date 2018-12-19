class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self,nbr, weight = 0):
        self.connectedTo[nbr]=weight

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id) + ' connected to : ' + str([ x for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self,fromVert,toVert,weight=0):
        if fromVert not in self.vertList:
            newVert = self.addVertex(fromVert)
        if toVert not in self.vertList:
            newVert = self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self, n):
        return n in self.vertList

g = Graph()   

for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,100)

print (g.vertList)

for vertex in g:
    print vertex
    print vertex.getConnections()
    print "\n"