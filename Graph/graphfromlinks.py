from graph import Graph
from graph import Node

def fromLinks(links):
    '''
    Takes a list of links in the form of tuples, or lists, 
    with two elements describing the connected nodes and returns a Graph.
    The element can be two simple node, like ('a', 'b') or a vertex and a node
    like (a, Node(2, 'b')).
    If weight is not specified, the edge weight default to 1
    
    Exampple input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]
    
    Example output: 
    (from first input):
    graph G {
        1
        1 -- 2 [label=1]
        1 -- 4 [label=1]
        2
        2 -- 1 [label=1]
        2 -- 3 [label=1]
        4
        4 -- 1 [label=1]
        4 -- 3 [label=1]
        3
        3 -- 2 [label=1]
        3 -- 4 [label=1]
    }

    (from second input:)
    graph G {
        1
        1 -- 2 [label=1]
        1 -- 4 [label=1]
        2
        2 -- 1 [label=1]
        4
        4 -- 1 [label=1]
        4 -- 3 [label=1]
        3
        3 -- 4 [label=1]
    }
    '''
    g = Graph()
    for link in links:
        firstVertex = link[0]
        node = link[1]
        secondVertex = node
        weight = 1 
        try:
            secondVertex = node.value
            weight = node.weight
        except AttributeError:
            pass
        if firstVertex is None and not secondVertex is None:
            g.addVertex(secondVertex)
        elif secondVertex is None and not firstVertex is None:
            g.addVertex(firstVertex)
        elif not firstVertex is None and not secondVertex is None:
            g.addEdge(firstVertex, secondVertex, weight)
    return g

if __name__ == "__main__":
    g = fromLinks([(1,2),(1,4),(2,3),(3,4)])

    g2 = Graph({
        1: [Node(1, 2), Node(1, 4)],
        2: [Node(1,1), Node(1,3)],
        3: [Node(1,2), Node(1,4)],
        4: [Node(1, 1), Node(1,3)]
    })

    if(g == g2):
        print("Graph from link created:")
        print(g)
    else:
        print("Failed to create the graph")
    g = fromLinks( [[1,2],[1,4],(None,3),(3,4)] )
    g2 = Graph({
        1: [Node(1, 2), Node(1, 4)],
        2: [Node(1,1)],
        3: [Node(1,4)],
        4: [Node(1,1), Node(1,3)]
    })
    if(g == g2):
        print("Graph from link created:")
        print(g)
    else:
        print("Failed to create the graph")

    g = fromLinks( [('a', Node(2.5, 'b')), ('a', Node(6.5, 'c')) ])
    g2 = Graph({
        'a' : [Node(2.5, 'b'), Node(6.5, 'c')],
        'b' : [Node(2.5, 'a')],
        'c' : [Node(6.5, 'a')]
    })

    if(g == g2):
        print("Graph from link created:")
        print(g)
    else:
        print("Failed to create the graph")