import unittest
from graph import Node
from graph import Graph

class TestGraphUnitTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()