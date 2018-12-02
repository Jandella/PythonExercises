class Node:
    "Node class for weighted graph"
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __eq__(self, other):
        if other is None:
            return False
        return self.weight == other.weight and other.value == self.value
    
    def __str__(self):
        "string representation of weighted node in .dot"
        return "%s [label=%d]" %(self.value, self.weight)

    def __repr__(self):
        return "{ value: %s, weight: %d }" %(self.value, self.weight)
    
    def __hash__(self):
        return hash(str(self))

class Graph:
    """Graph as dictionary (following Tutorials Points 
    https://www.tutorialspoint.com/python/python_graphs.htm)"""
    def __init__(self, dictGraph=None):
        if dictGraph is None:
            dictGraph = {}
        self.gdict = dictGraph
        for vertex in dictGraph:
            self.addVertex(vertex)
            for element in dictGraph[vertex]:
                self.addEdge(vertex, element.value, element.weight)
    
    def getVertices(self):
        return list(self.gdict.keys())
    
    def findEdges(self):
        res = [] #to store the result
        for vertex in self.gdict:
            for edge in self.gdict[vertex]:
                if {vertex, edge.value} not in res:
                    res.append({vertex, edge.value})
        return res

    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
    
    def addEdge(self, firstVertex, secondVertex, weight):
        if firstVertex not in self.gdict:
            self.gdict[firstVertex] = [Node(weight, secondVertex)]
        else:
            newnode = Node(weight, secondVertex)
            found = False
            for nodes in self.gdict[firstVertex]:
                if nodes.value == newnode.value:
                    found = True
                    break
            if not found:
                self.gdict[firstVertex].append(newnode)
        if secondVertex not in self.gdict:
            self.gdict[secondVertex] = [Node(weight, secondVertex)]
        else:
            newnode = Node(weight, firstVertex)
            found = False
            for nodes in self.gdict[secondVertex]:
                if nodes.value == newnode.value:
                    found = True
                    break
            if not found:
                self.gdict[secondVertex].append(newnode)

    def __str__(self):
        "string representation of a undirected graph in .dot"
        visited = {}
        res = "graph G {\n"
        for vertex in self.gdict:
            res += "\t" + vertex + "\n"
            for edge in self.gdict[vertex]:
                if not vertex in visited:
                    res += "\t" + vertex + " -- " + str(edge) + "\n"
            visited[vertex] = True    
        res += "}"
        return res

    def __eq__(self, other):
        res = False
        if(other is None):
            return res
        selfvertex = self.getVertices()
        othervertex = other.getVertices()
        if set(selfvertex) == set(othervertex):
            #edges are nodes, and findEdges return a list of nodes
            edgeSelf = self.findEdges()
            edgeOther = self.findEdges()
            if(len(edgeSelf) == len(edgeOther)):
                for edge in edgeSelf:
                    if edge not in edgeOther:
                        res = False
                        break
                    res = True
            else:
                res = False
        else:
            res = False
        return res


if __name__ == "__main__":
    graph_elements = { "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(1, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                }
    g = Graph(graph_elements)
    print(g.getVertices())
    print(g.findEdges())
    g.addEdge('a', 'e', 2)
    g.addEdge('a', 'c', 2)
    g.addEdge('f', 'a', 4)
    print(g.findEdges())
    print(g)