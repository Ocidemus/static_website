import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test2(self):
        node = TextNode("click here", TextType.LINK,"https://www.example.com")
        node2 = TextNode("click here", TextType.LINK,"https://www.example.com")
        self.assertEqual(node,node2)
    
    def test3(self):
        
        node = TextNode("click here", TextType.LINK,"https://www.example.com")
        node2 = TextNode("click here", TextType.BOLD,"https://www.example.com")
        self.assertNotEqual(node,node2)

    def test4 (self):
        node = TextNode("click here", TextType.LINK,"https://www.example.com")
        node2 = TextNode("click here", TextType.LINK,None)
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
