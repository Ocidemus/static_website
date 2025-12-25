from platform import node
import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
      
      
      
      #### HTML NODE TESTS ####  
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    
    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
    
    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, url="https://www.example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.png", "alt": "An image"})
        self.assertEqual(html_node.value, "")
    
    def test_link(self):
        node = TextNode("Click here", TextType.LINK, url="https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})
        self.assertEqual(html_node.value, "Click here")
    

    
        
        
if __name__ == "__main__":
    unittest.main()