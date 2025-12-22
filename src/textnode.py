from enum import Enum

from htmlnode import LeafNode
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url  
        
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag ="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag = "a", value=text_node.text, props ={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag= "img", value="", props = {"src": text_node.url, "alt": text_node.text})
    
def split_nodes_delimiter(text_nodes,delimiter, text_type):

    result = []
    for node in text_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Delimiter split resulted in uneven parts.")

            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i%2 == 0:
                    result.append(TextNode(part, TextType.TEXT))
                else:
                    result.append(TextNode(part, text_type))
        else:
            result.append(node)
    return result