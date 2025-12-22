from platform import node
import unittest

from textnode import TextNode, TextType, split_nodes_delimiter , text_node_to_html_node


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
    


    #### DELIMITER TESTS ####
    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("This is a **bold** statement.", TextType.TEXT),
            TextNode(" And this is normal text.", TextType.TEXT),
            TextNode(" And this is _italic_ text.", TextType.TEXT),
            TextNode(" And this is `code` text.", TextType.TEXT),
            TextNode(" this is to test the **end**", TextType.TEXT),
            TextNode(".", TextType.TEXT),
            TextNode(" Another **bold** and _name_ and `hello` here.", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        result2 = split_nodes_delimiter(result, "_", TextType.ITALIC)
        result3 = split_nodes_delimiter(result2, "`", TextType.CODE)
        
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" statement.", TextType.TEXT),
            TextNode(" And this is normal text.", TextType.TEXT),
            TextNode(" And this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
            TextNode(" And this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
            TextNode(" this is to test the ", TextType.TEXT),
            TextNode("end", TextType.BOLD),
            TextNode(".", TextType.TEXT),
            TextNode(" Another ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("name", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("hello", TextType.CODE),
            TextNode(" here.", TextType.TEXT)
        ]
        self.assertEqual(result3, expected)

if __name__ == "__main__":
    unittest.main()