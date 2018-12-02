import unittest
from graph import Node
from graph import Graph

class TestGraphUnitTest(unittest.TestCase):

    def test_constructor(self):
        graph_elements = { "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(3, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a")],
                "d" : []
                }
        g = Graph(graph_elements)
        expected = Graph({
            'a': [Node(1, 'b'), Node(2, 'c')],
            'b': [Node(1, 'a'), Node(1.5, 'd')],
            'c': [Node(2, 'a')],
            'd': []
        })
        
        self.assertTrue(g == expected, "Constructor not behaving correctly")

    def test_add_vertex(self):
        g = Graph()
        g.addVertex('a')
        g2 = Graph({ 'a': []})
        self.assertTrue(g, g2)

    def test_equals_null(self):
        g = Graph()
        self.assertFalse(g == None)

    def test_equals_true(self):
        graph_elements = { "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(1, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                }
        g = Graph(graph_elements)
        g2 = Graph(graph_elements.copy())
        self.assertEqual(g, g2)

    def test_equals_false(self):
        graph_elements = { "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(1, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                }
        g = Graph(graph_elements)
        g2 = Graph({'a': []})
        self.assertNotEqual(g,g2)

    def test_equals_false_different_weight(self):
        graph_elements = { "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(1, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                }
        g = Graph(graph_elements)
        g2 = Graph({ "a" : [Node(2,"b"), Node(2,"c")],
                "b" : [Node(2, "a"), Node(1.5, "d")],
                "c" : [Node(4,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                })
        self.assertNotEqual(g,g2, "Two graph with same edges but different weight should be not equal")

    def test_add_edge(self):
        g = Graph({'a': []})
        g.addEdge('a', 'b', 1)
        g2 = Graph({
            'a' : [Node(1, 'b')],
            'b' : [Node(1, 'a')]
        })
        self.assertEqual(g, g2, "Graph g different than graph g2")
    
    def test_add_edge_existing_edge(self):
        #should not add another edge
        g = Graph({
            'a' : [Node(1, 'b')],
            'b' : [Node(1, 'a')]
        })
        expected = Graph({
            'a' : [Node(1, 'b')],
            'b' : [Node(1, 'a')]
        })

        g.addEdge('b', 'a', 3)

        self.assertEqual(g, expected, "After adding existing edge the graph is different")
    def test_find_edges_one_edge(self):
        g = Graph({
            'a' : [Node(1, 'b')],
            'b' : [Node(1, 'a')]
        })
        edges = g.findEdges()
        self.assertEqual(len(edges), 1, "Not a single edge")

    def test_find_edge_five_edges(self):
        g = Graph({ "a" : [Node(1,"b"), Node(2,"c")],
                "b" : [Node(1, "a"), Node(1.5, "d")],
                "c" : [Node(2,"a"), Node(4.5, "d")],
                "d" : [Node(3, "e")],
                "e" : [Node(3, "d")]
                })
        edges = g.findEdges()
        self.assertEqual(len(edges), 5, "Not five edges")

if __name__ == '__main__':
    unittest.main()