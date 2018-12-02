import unittest
from graph import Node

class TestNodeMethods(unittest.TestCase):

    def test_eq_null(self):
        self.assertFalse(Node(2, 'a') == None)

    def test_eq_true(self):
        firstnode = Node(2, 'a')
        secondnode = Node(2, 'a')
        self.assertTrue(firstnode == secondnode)

    def test_eq_false_all_different(self):
        firstnode = Node(2, 'a')
        secondnode = Node(1.5, 'b')
        self.assertFalse(firstnode == secondnode)
    
    def test_eq_false_weight_different(self):
        firstnode = Node(2, 'a')
        secondnode = Node(3, 'a')
        self.assertFalse(firstnode == secondnode)
    
    def test_eq_false_value_different(self):
        firstnode = Node(2, 'a')
        secondnode = Node(2, 'b')
        self.assertFalse(firstnode == secondnode)


if __name__ == '__main__':
    unittest.main()