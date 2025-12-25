from inline_to_markdown import split_nodes_delimiter , extract_markdown_images , extract_markdown_links , split_nodes_image
from textnode import TextNode, TextType
import unittest

class TestInlineMarkdown(unittest.TestCase):
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

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com) inside."
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )




if __name__ == "__main__":
    unittest.main()